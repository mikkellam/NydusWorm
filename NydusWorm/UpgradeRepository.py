class UpgradeRepository:
    """repository storing all upgrade data as a dictionary of {int:UpgradeData}"""
    def __init__(self, upgrade_list):
        self.upgrade_dict = {}
        for upgrade in upgrade_list:
            self.upgrade_dict.update({upgrade.upgrade_id: upgrade})

    def get(self, upgrade_id):
        """
        get upgrade by id
        :param upgrade_id: id of UpgradeData
        :return: UpgradeData
        """
        return self.upgrade_dict.get(upgrade_id)

    def get_all(self):
        """get all UpgradeData objects"""
        return self.upgrade_dict.values()

