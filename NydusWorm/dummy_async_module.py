import os
dir_path = os.path.dirname(os.path.realpath(__file__))
import sys
sys.path.insert(0, dir_path + "/protocol")
import common_pb2
import abathur_pb2
from IntelManager import IntelManager
import BlizzardConstants
from i_async_module import IAsyncModule
import time
import IntelManager
import threading

class dummy_async_module(IAsyncModule):
    """description of class"""

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
        print("Lul, only initialising? I've got ages before i need to do anything")

    def game_start(self):
        self.game_running = True

        self.prod_man.queue_unit(BlizzardConstants.UNIT_BARRACKS, spacing=2)
        self.prod_man.queue_tech(BlizzardConstants.RESEARCH_COMBAT_SHIELD)
        self.prod_man.queue_unit(BlizzardConstants.UNIT_BARRACKS, spacing=2)
        self.prod_man.queue_unit(BlizzardConstants.UNIT_BARRACKS, spacing=2)
        self.prod_man.queue_unit(BlizzardConstants.UNIT_BARRACKS, spacing=2)
        for i in range(0, 10):
            self.prod_man.queue_unit(BlizzardConstants.UNIT_MARINE)

        for colony in self.intel_man.colonies:
            if colony.is_starting_location:
                self.e_start = colony.point

        self.the_gang = self.intel_man.squad_repository.create("TheGang")
        self.intel_man.handler.register_handler(abathur_pb2.UnitAddedSelf, lambda u: self.the_gang.add_unit(u))
        self.intel_man.handler.register_handler(abathur_pb2.StructureAddedSelf, lambda u: print(u.tag()))

        self.t = threading.Thread(target=self.request_every, args=[5])
        self.t.start()
        print("Wait... We started!?!??! FUCK! GIVE ME INTEL NOW!")

    def game_ended(self):
        self.game_running = False
        self.proxy_man.restart_game()
        print("Not. My. Fault...")

    def restart(self):
        self.done = False
        self.e_start = common_pb2.Point2D()
        self.t = None
        print("Good, I wasn't ready we needed to restart")

    def request_every(self, delay):
        while self.game_running:
            self.request_intel_update()
            for worker in self.intel_man.get_workers_self():
                self.the_gang.add_unit(worker)

            if len(self.the_gang.units) >= 22 and not self.done:
                print("attacking")
                self.combat.attack_move_squad(self.the_gang.id, self.e_start)
                self.done = True

            time.sleep(delay)
        print("It is over Jim")


