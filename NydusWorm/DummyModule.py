import os
dir_path = os.path.dirname(os.path.realpath(__file__))
import sys
sys.path.insert(0, dir_path + "/protocol")
import common_pb2
import abathur_pb2
import IModule
from IntelManager import IntelManager
import BlizzardConstants


class DummyModule(IModule.IModule):
    """Example implementation of a step module in python. builds 4 barracks and 10 marines
       then all ins with workers and marines"""
    def __init__(self, production_manager, intel_manager, combat_manager):
        self.prod_man = production_manager
        assert isinstance(intel_manager, IntelManager)
        self.intel = intel_manager
        self.combat = combat_manager
        self.done = False
        self.e_start = common_pb2.Point2D()

    def initialise(self):
        print("Module uses Initialise! \n... \n... \nNothing Happens...")

    def game_start(self):
        # Queue 4 barracks and 10 marines using the ProductionManager and BlizzardConstants
        self.prod_man.queue_unit(BlizzardConstants.UNIT_BARRACKS, spacing=2)
        self.prod_man.queue_unit(BlizzardConstants.UNIT_BARRACKS, spacing=2)
        self.prod_man.queue_unit(BlizzardConstants.UNIT_BARRACKS, spacing=2)
        self.prod_man.queue_unit(BlizzardConstants.UNIT_BARRACKS, spacing=2)
        for i in range(0, 10):
            self.prod_man.queue_unit(BlizzardConstants.UNIT_MARINE)

        # Find enemy starting location
        for colony in self.intel.colonies:
            if colony.is_starting_location:
                self.e_start = colony.point

        # Create a squad to more easily control units
        self.the_gang = self.intel.squad_repository.create("TheGang")
        # Everytime a unit is created, add it to the squad
        self.intel.handler.register_handler(abathur_pb2.UnitAddedSelf, lambda u: self.the_gang.add_unit(u))

    def game_step(self):
        # Add all workers to the squad
        for worker in self.intel.get_workers_self():
            self.the_gang.add_unit(worker)

        # Attack first time we control 22 units.(12 workers 10 marines)
        if len(self.the_gang.units) >= 22 and not self.done:
            self.combat.attack_move_squad(self.the_gang.id, self.e_start)
            self.done = True

    def game_ended(self):
        print("Module uses game_ended! \n... \n... \nNothing Happens...")

    def restart(self):
        self.done = False
        self.e_start = common_pb2.Point2D()
