import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
import sys
sys.path.insert(0, dir_path + "/protocol")
import score_pb2
import sc2api_pb2
import abathur_pb2
from Colony import Colony
from IntelUnit import IntelUnit
from SquadRepository import SquadRepository
import CaseHandler

class IntelManager:
    """Stores data about the current game state"""
    game_loop = 0

    def __init__(self):
        self.map = abathur_pb2.AbathurMap()  # TODO this is an empty datastructe atm
        self.score = score_pb2.Score()
        self.common = sc2api_pb2.PlayerCommon()
        self.handler = CaseHandler.CaseHandler() #TODO not being used yet.
        self.upgrades_self = []
        self.buildings_self = {}  # uint -> intelUnit
        self.units_self = {}  # uint -> intelUnit
        self.workers_self = {}  # uint -> intelUnit
        self.destructibles = {}  # uint -> intelUnit
        self.structures_enemy = {}  # uint -> intelUnit
        self.units_enemy = {}  # uint -> intelUnit
        self.workers_enemy = {}  # uint -> intelUnit
        self.primary_colony = Colony()
        self.colonies = []
        self.mineral_fields = {}  # uint -> intelUnit
        self.vespene_geysers = {}  # uint -> intelUnit
        self.production_queue = []
        self.squad_repository = SquadRepository()

    def update_intel(self, intel):
        if intel.HasField("map"):
            self.map.CopyFrom(intel.map)  # TODO this is an empty datastructure atm
        if intel.HasField("score"):
            self.score.CopyFrom(intel.score)
        if intel.HasField("common"):
            self.common.CopyFrom(intel.common)
        if len(intel.upgrades_self) > 0:
            self.upgrades_self = intel.upgrades_self

        self.game_loop = intel.game_loop

        for building in intel.buildings_self:
            self.buildings_self.update({building.tag: IntelUnit(building, self.game_loop)})

        for unit in intel.units_self:
            self.units_self.update({unit.tag: IntelUnit(unit, self.game_loop)})

        for worker in intel.workers_self:
            self.workers_self.update({worker.tag: IntelUnit(worker, self.game_loop)})

        for destructible in intel.destructibles:
            self.destructibles.update({destructible.tag: IntelUnit(destructible, self.game_loop)})

        for structure in intel.structures_enemy:
            self.structures_enemy.update({structure.tag: IntelUnit(structure, self.game_loop)})

        for unit in intel.units_enemy:
            self.units_enemy.update({unit.tag: IntelUnit(unit, self.game_loop)})

        for worker in intel.workers_enemy:
            self.workers_enemy.update({worker.tag: IntelUnit(worker, self.game_loop)})

        if intel.HasField("primary_colony"):
            self.primary_colony.update(intel.primary_colony)

        for colony in intel.colonies:
            col = Colony()
            col.update(colony)
            self.colonies.append(col)

        for mineral in intel.mineral_fields:
            self.mineral_fields.update({mineral.tag: IntelUnit(mineral, self.game_loop)})

        for vespene in intel.vespene_geysers:
            self.vespene_geysers.update({vespene.tag: IntelUnit(vespene, self.game_loop)})

        if len(intel.production_queue) > 0:
            self.production_queue = intel.production_queue

        for squad_data in intel.squads:
            squad = self.squad_repository.internal_update(squad_data.squad_id, squad_data.name)
            for unit in squad_data.units:
                squad.units.add(IntelUnit(unit, self.game_loop))

        for event in intel.events:
            self.handler.handle(event.case_type, self.try_get(event.unit_tag))

    def set_intel_empty(self):
        self.map = abathur_pb2.AbathurMap() #TODO this is an empty datastructe atm
        self.score = score_pb2.Score()
        self.common = sc2api_pb2.PlayerCommon()
        self.handler = CaseHandler.CaseHandler()
        self.upgrades_self = []
        self.buildings_self = {}            # uint -> intelUnit
        self.units_self = {}                # uint -> intelUnit
        self.workers_self = {}              # uint -> intelUnit
        self.destructibles = {}             # uint -> intelUnit
        self.structures_enemy = {}          # uint -> intelUnit
        self.units_enemy = {}                # uint -> intelUnit
        self.workers_enemy = {}             # uint -> intelUnit
        self.primary_colony = Colony()
        self.colonies = []
        self.mineral_fields = {}            # uint -> intelUnit
        self.vespene_geysers = {}           # uint -> intelUnit
        self.production_queue = []

    def get_minerals(self):
        return self.mineral_fields.values()

    def try_get_vespene_geysers(self, tag):
        return self.vespene_geysers.get(tag)

    def get_vespene_geysers(self):
        return self.vespene_geysers.values()

    def try_get_building_self(self, tag):
        return self.buildings_self.get(tag)

    def get_buildings_self(self):
        return self.buildings_self.values()

    def try_get_units_self(self,tag):
        return self.units_self.get(tag)

    def get_units_self(self):
        return self.units_self.values()

    def try_get_worker_self(self,tag):
        return self.workers_self.get(tag)

    def try_get(self, tag):
        res = self.units_self.get(tag)
        if res is not None:
            return res
        res = self.buildings_self.get(tag)
        if res is not None:
            return res
        res = self.workers_self.get(tag)
        if res is not None:
            return res
        res = self.structures_enemy.get(tag)
        if res is not None:
            return res
        res = self.units_enemy.get(tag)
        if res is not None:
            return res
        res = self.workers_enemy.get(tag)
        if res is not None:
            return res
        res = self.destructibles.get(tag)
        if res is not None:
            return res
        res = self.mineral_fields.get(tag)
        if res is not None:
            return res
        res = self.vespene_geysers.get(tag)
        if res is not None:
            return res

    def get_workers_self(self):
        return self.workers_self.values()

    def try_get_destructible(self, tag):
        return self.destructibles.get(tag)

    def get_destructibles(self):
        return self.destructibles.values()

    def get_structures_enemy(self):
        return self.structures_enemy.values()

    def get_units_enemy(self):
        return self.units_enemy.values()

    def get_workers_enemy(self):
        return self.workers_enemy.values()

    def structures_enemy_visible(self):
        for structure in self.structures_enemy:
            if structure.last_seen == self.game_loop:
                yield structure

    def units_enemy_visible(self):
        for unit in self.units_enemy:
            if unit.last_seen == self.game_loop:
                yield unit

    def workers_enemy_visible(self):
        for worker in self.workers_enemy:
            if worker.last_seen == self.game_loop:
                yield worker

    def buildings_self(self, *types):
        for structure in self.buildings_self.values():
            if structure.unit_type in types:
                yield structure

    def units_self(self, *types):
        for unit in self.units_self.values():
            if unit.unit_type in types:
                yield unit
