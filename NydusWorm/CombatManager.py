import os
dir_path = os.path.dirname(os.path.realpath(__file__))
import sys
sys.path.insert(0, dir_path + "/protocol")

import common_pb2
import sc2api_pb2
import abathur_pb2
import data_pb2
from ICombatManager import ICombatManager


class CombatManager(ICombatManager):
    def __init__(self, proxy_manager):
        self.proxy_man = proxy_manager

    def move_unit(self, unit_tag, point, queue=False):
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.MoveUnit()
        move_unit.unit_tag = unit_tag
        move_unit.point.CopyFrom(point)
        move_unit.queue = queue
        combat_req.move_unit.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def move_squad(self, squad_id, point, queue=False):
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.MoveSquad()
        move_unit.squad = squad_id
        move_unit.point.CopyFrom(point)
        move_unit.queue = queue
        combat_req.move_squad.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def attack_move_unit(self, unit_tag, point, queue=False):
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.AttackMoveUnit()
        move_unit.unit_tag = unit_tag
        move_unit.point.CopyFrom(point)
        move_unit.queue = queue
        combat_req.attack_move_unit.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def attack_move_squad(self, squad_id, point, queue=False):
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.AttackMoveSquad()
        move_unit.squad = squad_id
        move_unit.point.CopyFrom(point)
        move_unit.queue = queue
        combat_req.attack_move_squad.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def attack_unit(self, attacking_unit_tag, target_unit_tag, queue=False):
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.AttackUnit()
        move_unit.source_unit = attacking_unit_tag
        move_unit.target_unit = target_unit_tag
        move_unit.queue = queue
        combat_req.attack_unit.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def attack_squad(self, squad_id, target_unit_tag, queue=False):
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.AttackSquad()
        move_unit.squad = squad_id
        move_unit.target_unit = target_unit_tag
        move_unit.queue = queue
        combat_req.attack_squad.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def use_targeted_ability_unit(self, ability_id, using_unit_tag, target_unit_tag, queue=False):
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.UseTargetedAbilityUnit()
        move_unit.source_unit = using_unit_tag
        move_unit.target_unit = target_unit_tag
        move_unit.queue = queue
        combat_req.use_targeted_ability_unit.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def use_targeted_ability_squad(self, ability_id, squad_id, target_unit_tag, queue=False):
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.UseTargetedAbilitySquad()
        move_unit.squad = squad_id
        move_unit.target_unit = target_unit_tag
        move_unit.queue = queue
        combat_req.use_targeted_ability_squad.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def use_point_centered_ability_unit(self, ability_id, using_unit_tag, point, queue=False):
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.UsePointCenteredAbilityUnit()
        move_unit.source_unit = using_unit_tag
        move_unit.point.CopyFrom(point)
        move_unit.queue = queue
        combat_req.use_point_centered_ability_unit.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def use_point_centered_ability_squad(self, ability_id, squad_id, point, queue=False):
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.UsePointCenteredAbilitySquad()
        move_unit.squad = squad_id
        move_unit.point.CopyFrom(point)
        move_unit.queue = queue
        combat_req.use_point_centered_ability_squad.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def use_targetless_ability_unit(self, ability_id, unit_tag, queue=False):
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.UseTargetlessAbilityUnit()
        move_unit.source_unit = unit_tag
        move_unit.queue = queue
        combat_req.use_targetless_ability_unit.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def use_targetless_ability_squad(self, ability_id, squad_id, queue=False):
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.UseTargetlessAbilitySquad()
        move_unit.squad = squad_id
        move_unit.queue = queue
        combat_req.use_targetless_ability_squad.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def smart_move_unit(self, unit_tag, point, queue=False):
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.SmartMoveUnit()
        move_unit.unit_tag = unit_tag
        move_unit.point.CopyFrom(point)
        move_unit.queue = queue
        combat_req.smart_move_unit.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def smart_move_squad(self, squad_id, point, queue=False):
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.SmartMoveSquad()
        move_unit.squad = squad_id
        move_unit.point.CopyFrom(point)
        move_unit.queue = queue
        combat_req.smart_move_squad.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def smart_attack_move_unit(self, unit_tag, point, queue=False):
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.SmartAttackMoveUnit()
        move_unit.unit_tag = unit_tag
        move_unit.point.CopyFrom(point)
        move_unit.queue = queue
        combat_req.smart_attack_move_unit.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def smart_attack_move_squad(self, squad_id, point, queue=False):
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.SmartAttackMoveSquad()
        move_unit.squad = squad_id
        move_unit.point.CopyFrom(point)
        move_unit.queue = queue
        combat_req.smart_attack_move_squad.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def smart_attack_unit(self, attacking_unit_tag, target_unit, queue=False):
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.SmartAttackUnit()
        move_unit.source_unit = attacking_unit_tag
        move_unit.target_unit = target_unit
        move_unit.queue = queue
        combat_req.smart_attack_unit.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def smart_attack_squad(self, squad_id, target_unit, queue=False):
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.SmartAttackSquad()
        move_unit.squad = squad_id
        move_unit.target_unit = target_unit
        move_unit.queue = queue
        combat_req.smart_attack_squad.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)


#point2d = common_pb2.Point2D()
#point2d.x = 39
#point2d.y = 39
#
#man = CombatManager()
#print(man.move_unit(40040, point2d))
#print(man.attack_move_unit(40040, point2d))
#print(man.attack_unit(40040, 30000))
#print(man.smart_move_unit(40040, point2d))
#print(man.smart_attack_move_unit(40040, point2d))
#print(man.smart_attack_unit(40040, 30000))
#print(man.use_targeted_ability_unit(40, 40040, 30000))
#print(man.use_point_centered_ability_unit(40, 40040, point2d))
#print(man.use_targetless_ability_unit(40, 40040))
#
#print(man.move_squad(4, point2d))
#print(man.attack_move_squad(4, point2d))
#print(man.attack_squad(4, 30000))
#print(man.smart_move_squad(4, point2d))
#print(man.smart_attack_move_squad(4, point2d))
#print(man.smart_attack_squad(4, 30000))
#print(man.use_targeted_ability_squad(40, 4, 30000))
#print(man.use_point_centered_ability_squad(40, 4, point2d))
#print(man.use_targetless_ability_squad(40, 4))
