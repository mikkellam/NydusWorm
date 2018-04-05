import os
dir_path = os.path.dirname(os.path.realpath(__file__))
import sys
sys.path.insert(0, dir_path + "/protocol")
import sc2api_pb2
import abathur_pb2
import IProductionManager


class ProductionManager(IProductionManager.IProductionManager):
    def __init__(self, proxy_manager):
        self.manager = proxy_manager

    def clear_build_order(self):
        clear_req = abathur_pb2.ClearBuildOrder()
        prod_req = abathur_pb2.ProductionRequest()
        prod_req.clear_build_order.CopyFrom(clear_req)
        self.manager.answers.put(prod_req)

    def queue_unit(self, unit, position=None, spacing=0, skippable=True):
        queue_u_req = abathur_pb2.QueueUnit()
        queue_u_req.unit_id = unit
        if position is not None:
            queue_u_req.pos.CopyFrom(position)
        queue_u_req.spacing = spacing
        queue_u_req.skippable = skippable
        prod_req = abathur_pb2.ProductionRequest()
        prod_req.queue_unit.CopyFrom(queue_u_req)
        self.manager.answers.put(prod_req)

    def queue_tech(self, upgrade, skippable=True):
        prod_req = abathur_pb2.ProductionRequest()
        queue_tech = abathur_pb2.QueueTech()
        queue_tech.upgrade_id = upgrade
        queue_tech.skippable = skippable
        prod_req.queue_tech.CopyFrom(queue_tech)
        self.manager.answers.put(prod_req)
