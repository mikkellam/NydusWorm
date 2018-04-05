class BuffRepository(object):
    """repository holding all buff data"""
    def __init__(self, buff_list):
        self.buff_dict = {}
        for buff in buff_list:
            self.buff_dict.update({buff.buff_id: buff})

    def get(self, buff_id):
        return self.buff_dict.get(buff_id)

    def get_all(self):
        return self.buff_dict.values()
