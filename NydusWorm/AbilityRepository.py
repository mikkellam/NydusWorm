
class AbilityRepository:
    """Repository holding all ability data"""
    def __init__(self, ability_list):
        self.ability_dict = {}
        for ability in ability_list:
            self.ability_dict.update({ability.ability_id: ability })

    def get(self, ability_id):
        return self.ability_dict.get(ability_id)

    def get_all(self):
        return self.ability_dict.values()
