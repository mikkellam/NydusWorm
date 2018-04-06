
class AbilityRepository:
    """Repository holding all ability data as a dictionary of {int:AbilityData}"""
    def __init__(self, ability_list):
        self.ability_dict = {}
        for ability in ability_list:
            self.ability_dict.update({ability.ability_id: ability })

    def get(self, ability_id):
        """
        get an AbilityData by its Id
        :param ability_id: Id of the ability
        :return: AbilityData
        """
        return self.ability_dict.get(ability_id)

    def get_all(self):
        """get all AbilityData objects"""
        return self.ability_dict.values()
