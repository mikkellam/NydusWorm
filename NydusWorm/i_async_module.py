import os
dir_path = os.path.dirname(os.path.realpath(__file__))
import sys
sys.path.insert(0, dir_path + "/protocol")
from abc import ABC, abstractmethod
import abathur_pb2
import threading

class IAsyncModule(ABC):

    def __init__(self, proxy_man):
        self.proxy_man = proxy_man

    @abstractmethod
    def initialise(self):
        """Callback method. Called when framework is launched"""
        print("implement initialise")

    @abstractmethod
    def game_start(self):
        """callback method. Called when the sc2 game is started"""
        print("implement game_start")

    def request_intel_update(self, mmap=True, score=True, common=True, upgrades_self=True,
                             buildings_self=True, units_self=True, workers_self=True,
                             destructibles=True, structures_enemy=True, units_enemy=True,
                             workers_enemy=True, primary_colony=True, colonies=True,
                             mineral_fields=True, VespeneGeysers=True, production_queue=True,
                             squads=True, game_loop=True):
        """method that requests an update of the intel database"""
        intel_req = abathur_pb2.IntelRequest()
        intel_req.map = mmap
        intel_req.score = score
        intel_req.common = common
        intel_req.upgrades_self = upgrades_self
        intel_req.buildings_self = buildings_self
        intel_req.units_self = units_self
        intel_req.workers_self = workers_self
        intel_req.destructibles = destructibles
        intel_req.structures_enemy = structures_enemy
        intel_req.units_enemy = units_enemy
        intel_req.workers_enemy = workers_enemy
        intel_req.primary_colony = primary_colony
        intel_req.colonies = colonies
        intel_req.mineral_fields = mineral_fields
        intel_req.VespeneGeysers = VespeneGeysers
        intel_req.production_queue = production_queue
        intel_req.squads = squads
        intel_req.game_loop = game_loop
        self.proxy_man.intel_received.clear()
        self.proxy_man.answers.put(intel_req)
        self.proxy_man.intel_received.wait()

    @abstractmethod
    def game_ended(self):
        """callback method. called when the sc2 game ends"""
        print("implement game_ended")

    @abstractmethod
    def restart(self):
        """callback method. called when the game restarts"""
        print("implement restart")

