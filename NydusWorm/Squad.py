import os
dir_path = os.path.dirname(os.path.realpath(__file__))
import sys
sys.path.insert(0, dir_path + "/protocol")
import abathur_pb2
import uuid


class Squad():
    def __init__(self, name):
        self.id = uuid.uuid4().int & (1<<64)-1
        self.name = name
        self.units = set()
        self.requests = []

    def add_unit(self, unit):
        combat_req = abathur_pb2.CombatRequest()
        squad_req = abathur_pb2.SquadRequest()
        add_units = abathur_pb2.AddUnits()
        add_units.tags.append(unit.tag())
        add_units.squad_id = self.id
        squad_req.add_units.CopyFrom(add_units)
        combat_req.squad_request.CopyFrom(squad_req)
        self.requests.append(combat_req)
        return self.units.add(unit)

    def add_units(self, units):
        added = 0
        tags = []
        for unit in units:
            self.units.add(unit)
            tags.append(unit.tag())
            added = added + 1
        combat_req = abathur_pb2.CombatRequest()
        squad_req = abathur_pb2.SquadRequest()
        add_units = abathur_pb2.AddUnits()
        add_units.tags.extend(tags)
        add_units.squad_id = self.id
        squad_req.add_units.CopyFrom(add_units)
        combat_req.squad_request.CopyFrom(squad_req)
        self.requests.append(combat_req)
        return added

    def remove_unit(self, unit):
        combat_req = abathur_pb2.CombatRequest()
        squad_req = abathur_pb2.SquadRequest()
        remove_units = abathur_pb2.RemoveUnits()
        remove_units.tags.append(unit.tag())
        remove_units.squad_id = self.id
        squad_req.remove_units.CopyFrom(remove_units)
        combat_req.squad_request.CopyFrom(squad_req)
        self.requests.append(combat_req)
        self.units.remove(unit)

    def remove_units(self, units):
        remove = 0
        tags = []
        for unit in units:
            self.units.remove(unit)
            tags.append(unit.tag())
            remove = remove + 1

        request = abathur_pb2.AbathurRequest()
        combat_req = request.combat.add()
        squad_req = abathur_pb2.SquadRequest()
        remove_units = abathur_pb2.RemoveUnits()
        remove_units.tags.extend(tags)
        remove_units.squad_id = self.id
        squad_req.remove_units.CopyFrom(remove_units)
        combat_req.squad_request.CopyFrom(squad_req)
        request.combat.CopyFrom(combat_req)
        self.requests.append(request)
        return remove

    def __str__(self):
        res = self.name + ": {"
        for u in self.units:
            res = res + u.tag() + ", " + u.unit_type()
        return res