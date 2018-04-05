class UpgradeRepository:
    """repository storing all upgrade data"""
    def __init__(self, upgrade_list):
        self.upgrade_dict = {}
        for upgrade in upgrade_list:
            self.upgrade_dict.update({upgrade.upgrade_id: upgrade})

    def get(self, upgrade_id):
        return self.upgrade_dict.get(upgrade_id)

    def get_all(self):
        return self.upgrade_dict.values()

