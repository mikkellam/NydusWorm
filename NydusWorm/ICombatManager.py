from abc import ABC, abstractmethod


class ICombatManager(ABC):
    @abstractmethod
    def move_unit(self, unit, point, queue = False):
        print("move_unit not implemented")

    @abstractmethod
    def move_squad(self, squad, point, queue = False):
        print("move_squad not implemented")

    @abstractmethod
    def attack_move_unit(self, unit, point, queue = False):
        print("attack_move_unit not implemented")

    @abstractmethod
    def attack_move_squad(self, squad, point, queue = False):
        print("attack_move_squad not implemented")

    @abstractmethod
    def attack_unit(self, attacking_unit, target_unit, queue = False):
        print("attack_unit not implemented")

    @abstractmethod
    def attack_squad(self, squad, taget_unit, queue = False):
        print("attack_squad not implemented")

    @abstractmethod
    def use_targeted_ability_unit(self, ability_id, using_unit, taget_unit, queue = False):
        print("use_targeted_ability_unit not implemented")

    @abstractmethod
    def use_targeted_ability_squad(self, ability_id, squad, target_unit, queue = False):
        print("use_target_ability_squad not implemented")

    @abstractmethod
    def use_point_centered_ability_unit(self, ability_id, using_unit, point, queue = False):
        print("use_point_centered_ability_unit not implemented")

    @abstractmethod
    def use_point_centered_ability_squad(self, ability_id, squad, point, queue = False):
        print("use_point_centered_ability_squad not implemented")

    @abstractmethod
    def use_targetless_ability_unit(self, ability_id, unit, queue = False):
        print("use_targetless_ability_unit not implemented")

    @abstractmethod
    def use_targetless_ability_squad(self, ability_id, squad, queue = False):
        print("use_targetless_ability_unit not implemented")

    @abstractmethod
    def smart_move_unit(self, unit, point, queue = False):
        """Smart move uses microcontroller written in c# and will not be different from regular move unless such a microcontroller is written"""
        print("smart_move_unit not implemented")

    @abstractmethod
    def smart_move_squad(self, squad, point, queue = False):
        """Smart move uses microcontroller written in c# and will not be different from regular move unless such a microcontroller is written"""
        print("smart_move_squad not implemented")

    @abstractmethod
    def smart_attack_move_unit(self, unit, point, queue = False):
        """Smart attack move uses microcontroller written in c# and will not be different from regular attack move unless such a microcontroller is written"""
        print("smart_attack_move_unit not implemented")

    @abstractmethod
    def smart_attack_move_squad(self, squad, point, queue = False):
        """Smart attack move uses microcontroller written in c# and will not be different from regular attack move unless such a microcontroller is written"""
        print("smart_attack_move_squad not implemented")

    @abstractmethod
    def smart_attack_unit(self, attacking_unit, target_unit, queue = False):
        """Smart attack uses microcontroller written in c# and will not be different from regular attack unless such a microcontroller is written"""
        print("smart_attack_unit not implemented")

    @abstractmethod
    def smart_attack_squad(self, squad, target_unit, queue = False):
        """Smart attack uses microcontroller written in c# and will not be different from regular attack unless such a microcontroller is written"""
        print("smart_attack_squad not implemented")
