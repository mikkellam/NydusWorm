import os
dir_path = os.path.dirname(os.path.realpath(__file__))
import sys
sys.path.insert(0, dir_path + "/protocol")
import abathur_pb2
from Squad import Squad


class SquadRepository:
    """Repository in charge managing squads"""
    def __init__(self):
        self.squads = {}
        self.requests = []

    def create(self, name):
        """
        Create a new squad with the given name
        :param name: name of the squad
        :return: The Created Squad
        """
        squad = Squad(name)
        combat_req = abathur_pb2.CombatRequest()
        squad_req = abathur_pb2.SquadRequest()
        squad_data = abathur_pb2.SquadData()
        squad_data.squad_id = squad.id
        squad_data.name = squad.name
        create_squad_req = abathur_pb2.CreateSquad()
        create_squad_req.squad.CopyFrom(squad_data)
        squad_req.create_squad.CopyFrom(create_squad_req)
        combat_req.squad_request.CopyFrom(squad_req)
        self.requests.append(combat_req)

        self.squads.update({squad.id: squad})
        return squad

    def internal_update(self, squad_id, name):
        """Internal method used to update squads with intel received from a IntelResponse
           UPDATES MADE WITH THIS METHOD WILL NOT BE SENT TO C# AND WILL BE OVERWRITTEN"""
        if self.squads.__contains__(squad_id):
            squad = self.squads.get(squad_id)
        else:
            squad = Squad(name)
            squad.id = squad_id
            self.squads.update({squad.id: squad})
        return squad

    def get_by_id(self, squad_id):
        for squad in self.squads:
            if int(squad.id) == squad_id:
                return squad

    def get_by_name(self, name):
        for squad in self.squads:
            if squad.name == name:
                return squad

    def get(self):
        return self.squads

    def remove(self, squad):
        """Remove given squad from the repository"""
        combat_req = abathur_pb2.CombatRequest()
        squad_req = abathur_pb2.SquadRequest()
        remove_squad_req = abathur_pb2.RemoveSquad()
        remove_squad_req.squad_id = squad.id
        squad_req.CopyFrom(remove_squad_req)
        combat_req.squad_req.CopyFrom(squad_req)
        self.requests.append(combat_req)

        del self.squads[squad.id]

    def internal_clear(self):
        self.squads = {}