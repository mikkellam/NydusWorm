class BuffRepository(object):
    """Repository holding all buff data as a dictionary of {int:BuffData}"""
    def __init__(self, buff_list):
        self.buff_dict = {}
        for buff in buff_list:
            self.buff_dict.update({buff.buff_id: buff})

    def get(self, buff_id):
        """
        Get a BuffData by its Id
        :param buff_id: Id of the buff
        :return: BuffData
        """
        return self.buff_dict.get(buff_id)

    def get_all(self):
        """Get all BuffData objects"""
        return self.buff_dict.values()
