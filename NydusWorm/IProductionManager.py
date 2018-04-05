from abc import ABC, abstractmethod


class IProductionManager(ABC):
    @abstractmethod
    def clear_build_order(self):
        print("clear_build_order not implemented")

    @abstractmethod
    def queue_unit(self, unit, position = None, skippable = True):
        print("queue_unit not implemented")

    @abstractmethod
    def queue_tech(self, upgrade, skippable = True):
        print("queue_tech not implemented")
