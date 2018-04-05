class UnitTypeRepository(object):
    """description of class"""
    def __init__(self, unit_types):
        self.unit_type_dict = {}
        for unit_type in unit_types:
            self.unit_type_dict.update({unit_type.unit_id: unit_type})

    def get(self, unit_id):
        return self.unit_type_dict.get(unit_id)

    def get_all(self):
        return self.unit_type_dict.values()