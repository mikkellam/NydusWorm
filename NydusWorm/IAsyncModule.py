import os
dir_path = os.path.dirname(os.path.realpath(__file__))
import sys
sys.path.insert(0, dir_path + "/protocol")
from abc import ABC, abstractmethod
import abathur_pb2

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

    def request_intel_update(self, wait=True, mmap=True, score=True, common=True, upgrades_self=True,
                             buildings_self=True, units_self=True, workers_self=True,
                             destructibles=True, structures_enemy=True, units_enemy=True,
                             workers_enemy=True, primary_colony=True, colonies=True,
                             mineral_fields=True, VespeneGeysers=True, production_queue=True,
                             squads=True, game_loop=True, feature_data=False, render_data=False,
                             ui_data=False):
        """
        method that requests an update of the IntelManager

        :param wait: wait for a response?
        :param mmap: receive data about the map
        :param score: receive data about the score
        :param common: receive the PlayerCommon data object
        :param upgrades_self: receive what upgrades you have
        :param buildings_self: reveive what buildings you have
        :param units_self: receive what units you have
        :param workers_self: receive what workers you have
        :param destructibles: receive all destructible units
        :param structures_enemy: receive seen enemy structures
        :param units_enemy: receive seen enemy units
        :param workers_enemy: receive seen enemy workers
        :param primary_colony: receive data about your starting colony
        :param colonies: receive data about all colonies
        :param mineral_fields: receive data about all mineralfields
        :param VespeneGeysers: receive data about all vespene geysers
        :param production_queue: receive the production queue
        :param squads: receive all squads
        :param game_loop: receive the current gameloop
        :param feature_data: receive the data for the feature layer
        :param render_data: receive remder_data
        :param ui_data: receive ui data
        :return: None
        """
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
        intel_req.feature_layer_data = feature_data
        intel_req.render_data = render_data
        intel_req.ui_data = ui_data
        self.proxy_man.intel_received.clear()
        self.proxy_man.answers.put(intel_req)
        if wait:
            self.proxy_man.intel_received.wait()

    @abstractmethod
    def game_ended(self):
        """callback method. called when the sc2 game ends"""
        print("implement game_ended")

    @abstractmethod
    def restart(self):
        """callback method. called when the game restarts"""
        print("implement restart")

