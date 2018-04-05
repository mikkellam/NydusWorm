import sys
from NydusWorm import NydusWorm
from dummy_async_module import dummy_async_module
from dummy_module import DummyModule
from ProductionManager import ProductionManager
from CombatManager import CombatManager
from IntelManager import IntelManager


class DummyLauncher(NydusWorm):
    def add_modules(self, manager, services):
        prod_man = services.get(ProductionManager)
        combat_man = services.get(CombatManager)
        intel_man = services.get(IntelManager)
        #manager.add_module(DummyModule(prod_man, intel_man, combat_man))
        manager.add_module(dummy_async_module(manager, intel_man, combat_man, prod_man))


launcher = DummyLauncher()
launcher.launch_framework(sys.argv)
