import sys
from NydusWorm import NydusWorm
from DummyAsyncModule import DummyAsyncModule
from DummyModule import DummyModule
from ProductionManager import ProductionManager
from CombatManager import CombatManager
from IntelManager import IntelManager


class DummyLauncher(NydusWorm):
    """Example of a launcher class in python"""
    def add_modules(self, manager, services):
        prod_man = services.get(ProductionManager)
        combat_man = services.get(CombatManager)
        intel_man = services.get(IntelManager)
        #manager.add_module(DummyAsyncModule(manager, intel_man, combat_man, prod_man))
        manager.add_module(DummyModule(prod_man, intel_man, combat_man))


launcher = DummyLauncher()
launcher.launch_framework(sys.argv)
