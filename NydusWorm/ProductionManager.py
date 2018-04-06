import os
dir_path = os.path.dirname(os.path.realpath(__file__))
import sys
sys.path.insert(0, dir_path + "/protocol")
import abathur_pb2


class ProductionManager:
    """Service allowing for easy production of units and upgrades"""
    def __init__(self, proxy_manager):
        self.manager = proxy_manager

    def clear_build_order(self):
        """Empties the production queue"""
        clear_req = abathur_pb2.ClearBuildOrder()
        prod_req = abathur_pb2.ProductionRequest()
        prod_req.clear_build_order.CopyFrom(clear_req)
        self.manager.answers.put(prod_req)

    def queue_unit(self, unit, position=None, spacing=0, low_priority=False):
        """
        Queue a unit for production by the ProductionManager
        :param unit: Id of the UnitType you wish to produce
        :param position: The position at which you wish to produce the unit.(optional)
        :param spacing: The spacing you wish between this building and unplacable postions at construction time
        :param low_priority: queue the unit as low_priority meaning that it will be skipped if you can afford it but can afford something else in the queue
        :return: None
        """
        queue_u_req = abathur_pb2.QueueUnit()
        queue_u_req.unit_id = unit
        if position is not None:
            queue_u_req.pos.CopyFrom(position)
        queue_u_req.spacing = spacing
        queue_u_req.skippable = low_priority
        prod_req = abathur_pb2.ProductionRequest()
        prod_req.queue_unit.CopyFrom(queue_u_req)
        self.manager.answers.put(prod_req)

    def queue_tech(self, upgrade, low_priority=False):
        """
        :param upgrade: id of the upgrade you wish to produce
        :param low_priority: set a low priority meaning that it will be skipped if you cannot afford it right now
        :return: None
        """
        prod_req = abathur_pb2.ProductionRequest()
        queue_tech = abathur_pb2.QueueTech()
        queue_tech.upgrade_id = upgrade
        queue_tech.skippable = low_priority
        prod_req.queue_tech.CopyFrom(queue_tech)
        self.manager.answers.put(prod_req)
