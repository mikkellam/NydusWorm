from enum import Enum
from threading import Lock
lock = Lock()


class Case(Enum):
    """Enum indicating different types of events to which one can react"""
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
    """Class managing a set of handlers reacting to different "Case"'s"""
    def __init__(self):
        self.handlers = {}

    def handle(self, case, unit):
        """
        Call all handlers matching the specific case
        :param case: the Case indicating what event has happened
        :param unit: the IntelUnit with which something has happened
        :return: None
        """
        with lock:
            if self.handlers.__contains__(case):
                for h in self.handlers.get(case):
                    h(unit)

    def register_handler(self, case, handler):
        """
        Register a handler to be called when a specific case occurs
        :param case: The Case to which the handler to react to
        :param handler: The method that should be called when "case" happens
        :return: None
        """
        with lock:
            if self.handlers.__contains__(case):
                self.handlers.get(case).append(handler)
            else:
                self.handlers.update({case: [handler]})

    def deregister_handler(self, handler):
        """Make sure a specific handler is no longer called"""
        with lock:
            for case, hs in self.handlers.items():
                if hs.__contains__(handler):
                    hs.remove(handler)

