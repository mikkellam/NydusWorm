from enum import Enum
from threading import Lock
lock = Lock()

class Case(Enum):
    UnitAddedSelf = 1
    UnitAddedEnemy = 2
    UnitDestroyed = 3
    AddedHiddenEnemy = 4
    WorkerAddedSelf = 5
    WorkerAddedEnemy = 6
    WorkerDestroyed = 7
    StructureAddedSelf = 8
    StructureAddedEnemy = 9
    StructureDestroyed = 10
    MineralDepleted = 11


class CaseHandler:
    def __init__(self):
        self.handlers = {}

    def handle(self, case, unit):
        with lock:
            if self.handlers.__contains__(case):
                for h in self.handlers.get(case):
                    h(unit)

    def register_handler(self, case, handler):
        with lock:
            if self.handlers.__contains__(case):
                self.handlers.get(case).append(handler)
            else:
                self.handlers.update({case: [handler]})

    def deregister_handler(self, handler):
        with lock:
            for case, hs in self.handlers.items():
                if hs.__contains__(handler):
                    hs.remove(handler)

