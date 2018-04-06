class UnitTypeRepository(object):
    """Repository holding all UnitTypeData as a dictionary of {int:UnitTypeData}"""
    def __init__(self, unit_types):
        self.unit_type_dict = {}
        for unit_type in unit_types:
            self.unit_type_dict.update({unit_type.unit_id: unit_type})

    def get(self, unit_id):
        """
        get a UnitTypeData by its id
        :param unit_id: Id of UnitTypeData
        :return: UnitTypeData
        """
        return self.unit_type_dict.get(unit_id)

    def get_all(self):
        """get all UnitTypeData objects"""
        return self.unit_type_dict.values()
