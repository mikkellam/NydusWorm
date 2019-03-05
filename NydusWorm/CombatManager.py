import os
dir_path = os.path.dirname(os.path.realpath(__file__))
import sys
sys.path.insert(0, dir_path + "/protocol")

import abathur_pb2


class CombatManager:
    """Class allowing for issuing commands to units and squads such as attacking, moving or using an ability"""
    def __init__(self, proxy_manager):
        self.proxy_man = proxy_manager

    def move_unit(self, unit_tag, point, queue=False):
        """
        :param unit_tag: Tag of unit to be moved
        :param point: Point2D towards which there should be moved
        :param queue: Should the order be executed after existing ones(true) or overrule previous orders(false)?
        :return: None
        """
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.MoveUnit()
        move_unit.unit_tag = unit_tag
        move_unit.point.CopyFrom(point)
        move_unit.queue = queue
        combat_req.move_unit.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def move_squad(self, squad_id, point, queue=False):
        """
        :param squad_id: id of squad who should move
        :param point: Point2D towards which there should be moved
        :param queue: Should the order be executed after existing ones(true) or overrule previous orders(false)?
        :return: None
        """
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.MoveSquad()
        move_unit.squad = squad_id
        move_unit.point.CopyFrom(point)
        move_unit.queue = queue
        combat_req.move_squad.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def attack_move_unit(self, unit_tag, point, queue=False):
        """

        :param unit_tag: Tag of unit who should attack move
        :param point: Point2D towards which there should be attack moved
        :param queue: Should the order be executed after existing ones(true) or overrule previous orders(false)?
        :return: None
        """
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.AttackMoveUnit()
        move_unit.unit_tag = unit_tag
        move_unit.point.CopyFrom(point)
        move_unit.queue = queue
        combat_req.attack_move_unit.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def attack_move_squad(self, squad_id, point, queue=False):
        """
        :param squad_id: id of squad that should attack move
        :param point: Point2D towards which there should be attack moved
        :param queue: Should the order be executed after existing ones(true) or overrule previous orders(false)?
        :return: None
        """
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.AttackMoveSquad() # TODO fix temporary variable names
        move_unit.squad = squad_id
        move_unit.point.CopyFrom(point)
        move_unit.queue = queue
        combat_req.attack_move_squad.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def attack_unit(self, attacking_unit_tag, target_unit_tag, queue=False):
        """
        :param attacking_unit_tag: Tag of unit who should attack
        :param target_unit_tag: Tag of unit to attack
        :param queue: Should the order be executed after existing ones(true) or overrule previous orders(false)?
        :return: None
        """
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.AttackUnit()
        move_unit.source_unit = attacking_unit_tag
        move_unit.target_unit = target_unit_tag
        move_unit.queue = queue
        combat_req.attack_unit.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def attack_squad(self, squad_id, target_unit_tag, queue=False):
        """
        :param squad_id: id of squad that should attack
        :param target_unit_tag: tag of unit that should be attacked
        :param queue: Should the order be executed after existing ones(true) or overrule previous orders(false)?
        :return: None
        """
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.AttackSquad()
        move_unit.squad = squad_id
        move_unit.target_unit = target_unit_tag
        move_unit.queue = queue
        combat_req.attack_squad.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def use_targeted_ability_unit(self, ability_id, using_unit_tag, target_unit_tag, queue=False):
        """
        :param ability_id: id of the ability to be used
        :param using_unit_tag: tag of the unit using the ability
        :param target_unit_tag: tag of the unit the ability should be used on
        :param queue: Should the order be executed after existing ones(true) or overrule previous orders(false)?
        :return: None
        """
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.UseTargetedAbilityUnit()
        move_unit.ability_id = ability_id
        move_unit.source_unit = using_unit_tag
        move_unit.target_unit = target_unit_tag
        move_unit.queue = queue
        combat_req.use_targeted_ability_unit.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def use_targeted_ability_squad(self, ability_id, squad_id, target_unit_tag, queue=False):
        """
        :param ability_id: id of the ability to be used
        :param squad_id: id of the squad that should use the ability
        :param target_unit_tag: tag of the unit the ability should be used on
        :param queue: Should the order be executed after existing ones(true) or overrule previous orders(false)?
        :return: None
        """
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.UseTargetedAbilitySquad()
        move_unit.ability_id = ability_id
        move_unit.squad = squad_id
        move_unit.target_unit = target_unit_tag
        move_unit.queue = queue
        combat_req.use_targeted_ability_squad.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def use_point_centered_ability_unit(self, ability_id, using_unit_tag, point, queue=False):
        """
        :param ability_id: id of the ability to be used
        :param using_unit_tag: tag of unit using ability
        :param point: the point on which the ability should be used
        :param queue: Should the order be executed after existing ones(true) or overrule previous orders(false)?
        :return: None
        """
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.UsePointCenteredAbilityUnit()
        move_unit.ability_id = ability_id
        move_unit.source_unit = using_unit_tag
        move_unit.point.CopyFrom(point)
        move_unit.queue = queue
        combat_req.use_point_centered_ability_unit.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def use_point_centered_ability_squad(self, ability_id, squad_id, point, queue=False):
        """
        :param ability_id: id of the ability to be used
        :param squad_id: The id of the squad that should use the ability
        :param point: the point on which the ability should be used
        :param queue: Should the order be executed after existing ones(true) or overrule previous orders(false)?
        :return: None
        """
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.UsePointCenteredAbilitySquad()
        move_unit.ability_id = ability_id
        move_unit.squad = squad_id
        move_unit.point.CopyFrom(point)
        move_unit.queue = queue
        combat_req.use_point_centered_ability_squad.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def use_targetless_ability_unit(self, ability_id, unit_tag, queue=False):
        """
        :param ability_id: id of the ability to be used
        :param unit_tag: The unit that should use the ability
        :param queue: Should the order be executed after existing ones(true) or overrule previous orders(false)?
        :return: None
        """
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.UseTargetlessAbilityUnit()
        move_unit.ability_id = ability_id
        move_unit.source_unit = unit_tag
        move_unit.queue = queue
        combat_req.use_targetless_ability_unit.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def use_targetless_ability_squad(self, ability_id, squad_id, queue=False):
        """
        :param ability_id: id of the ability to be used
        :param squad_id: The squad that should use the ability
        :param queue: Should the order be executed after existing ones(true) or overrule previous orders(false)?
        :return: None
        """
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.UseTargetlessAbilitySquad()
        move_unit.ability_id = ability_id
        move_unit.squad = squad_id
        move_unit.queue = queue
        combat_req.use_targetless_ability_squad.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def smart_move_unit(self, unit_tag, point, queue=False):
        """
        Smart move uses microcontrollers written in c# and will not be different
         from regular move unless such a microcontroller is written
        :param unit_tag: tag of the unit that should move
        :param point: the point toward which the unit should move
        :param queue: Should the order be executed after existing ones(true) or overrule previous orders(false)?
        :return: None
        """
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.SmartMoveUnit()
        move_unit.unit_tag = unit_tag
        move_unit.point.CopyFrom(point)
        move_unit.queue = queue
        combat_req.smart_move_unit.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def smart_move_squad(self, squad_id, point, queue=False):
        """
        Smart move uses microcontrollers written in c# and will not be different
         from regular move unless such a microcontroller is written
        :param squad_id: id of the squadd that should move
        :param point: the point towards which the squad should move
        :param queue: Should the order be executed after existing ones(true) or overrule previous orders(false)?
        :return: None
        """
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.SmartMoveSquad()
        move_unit.squad = squad_id
        move_unit.point.CopyFrom(point)
        move_unit.queue = queue
        combat_req.smart_move_squad.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def smart_attack_move_unit(self, unit_tag, point, queue=False):
        """
        Smart attack move uses microcontrollers written in c# and will not be different
         from regular attack move unless such a microcontroller is written
        :param unit_tag: Tag of the unit that should attack move
        :param point: The point towards which the unit should attack move
        :param queue: Should the order be executed after existing ones(true) or overrule previous orders(false)?
        :return: None
        """
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.SmartAttackMoveUnit()
        move_unit.unit_tag = unit_tag
        move_unit.point.CopyFrom(point)
        move_unit.queue = queue
        combat_req.smart_attack_move_unit.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def smart_attack_move_squad(self, squad_id, point, queue=False):
        """
        Smart attack move uses microcontrollers written in c# and will not be different
         from regular attack move unless such a microcontroller is written
        :param squad_id: id of the squad that should attack move
        :param point: point towards which the squad should attack movve
        :param queue: Should the order be executed after existing ones(true) or overrule previous orders(false)?
        :return: None
        """
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.SmartAttackMoveSquad()
        move_unit.squad = squad_id
        move_unit.point.CopyFrom(point)
        move_unit.queue = queue
        combat_req.smart_attack_move_squad.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def smart_attack_unit(self, attacking_unit_tag, target_unit, queue=False):
        """
        Smart attack uses microcontrollers written in c# and will not be different
         from regular attack unless such a microcontroller is written
        :param attacking_unit_tag: tag of unit that should attack
        :param target_unit: tag of unit that should be attacked
        :param queue: Should the order be executed after existing ones(true) or overrule previous orders(false)?
        :return: None
        """
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.SmartAttackUnit()
        move_unit.source_unit = attacking_unit_tag
        move_unit.target_unit = target_unit
        move_unit.queue = queue
        combat_req.smart_attack_unit.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)

    def smart_attack_squad(self, squad_id, target_unit, queue=False):
        """
        Smart attack uses microcontrollers written in c# and will not be different
         from regular attack unless such a microcontroller is written
        :param squad_id: id of squad that should attack
        :param target_unit: tag of unit that should be attacked
        :param queue: Should the order be executed after existing ones(true) or overrule previous orders(false)?
        :return: None
        """
        combat_req = abathur_pb2.CombatRequest()
        move_unit = abathur_pb2.SmartAttackSquad()
        move_unit.squad = squad_id
        move_unit.target_unit = target_unit
        move_unit.queue = queue
        combat_req.smart_attack_squad.CopyFrom(move_unit)
        self.proxy_man.answers.put(combat_req)
