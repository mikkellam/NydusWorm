import os
dir_path = os.path.dirname(os.path.realpath(__file__))
import sys
sys.path.insert(0, dir_path + "/protocol")
import common_pb2
import abathur_pb2
from IntelManager import IntelManager
import BlizzardConstants
from IAsyncModule import IAsyncModule
import time
import IntelManager
import threading


class DummyAsyncModule(IAsyncModule):
    """Sample implementation of a async module in python. builds 4 barracks 10 marines and allins with the workers"""

    def __init__(self, proxy_man, intel_man, combat_manager, production_manager):
        IAsyncModule.__init__(self, proxy_man)
        assert isinstance(intel_man, IntelManager.IntelManager)
        self.intel_man = intel_man
        self.game_running = False
        self.prod_man = production_manager
        self.combat = combat_manager
        self.done = False
        self.e_start = common_pb2.Point2D()
        self.t = None

    def initialise(self):
        print("initializing")

    def game_start(self):
        self.game_running = True
        # Queue units for production using the ProductionManager and the BlizzardConstants
        self.prod_man.queue_unit(BlizzardConstants.UNIT_BARRACKS, spacing=2)
        self.prod_man.queue_tech(BlizzardConstants.RESEARCH_COMBAT_SHIELD)
        self.prod_man.queue_unit(BlizzardConstants.UNIT_BARRACKS, spacing=2)
        self.prod_man.queue_unit(BlizzardConstants.UNIT_BARRACKS, spacing=2)
        self.prod_man.queue_unit(BlizzardConstants.UNIT_BARRACKS, spacing=2)
        for i in range(0, 10):
            self.prod_man.queue_unit(BlizzardConstants.UNIT_MARINE)

        # Find the enemy startinng location
        for colony in self.intel_man.colonies:
            if colony.is_starting_location:
                self.e_start = colony.point

        # Create a squad for easier unit manipulation
        self.the_gang = self.intel_man.squad_repository.create("TheGang")

        # Register handler to react to new units being added
        self.intel_man.handler.register_handler(abathur_pb2.UnitAddedSelf, lambda u: self.the_gang.add_unit(u))

        # Start a thread for regularly checking the state of the game
        self.t = threading.Thread(target=self.request_every, args=[5])
        self.t.start()

    def game_ended(self):
        self.game_running = False

    def restart(self):
        self.done = False
        self.e_start = common_pb2.Point2D()
        self.t = None

    def request_every(self, delay):
        while self.game_running:
            # Request that the IntelManager is updated
            self.request_intel_update()
            # Add all workers to squad
            for worker in self.intel_man.get_workers_self():
                self.the_gang.add_unit(worker)
            # if we have produced all 10 marines we will have a total of 22 members of our squad
            # and the attack should start
            if len(self.the_gang.units) >= 22 and not self.done:
                self.combat.attack_move_squad(self.the_gang.id, self.e_start)
                self.done = True
            time.sleep(delay)
