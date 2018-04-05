import os
dir_path = os.path.dirname(os.path.realpath(__file__))
import sys
sys.path.insert(0, dir_path + "/protocol")

import common_pb2
import sc2api_pb2
import abathur_pb2
import data_pb2

class Colony:
    """class modeling a base with its mineral fields, vespene geyers, workers and buildings"""
    def __init__(self):
        self._id = 0
        self._point = common_pb2.Point2D()
        self._is_starting_location = False
        self._minerals = []
        self._vespene = []
        self._structures = []
        self._workers = []
        self._desired_vespene_workers = 0

    def update(self, colony_data):
        self._id = colony_data.col_id
        self._point = colony_data.point
        self._is_starting_location = colony_data.is_starting_location
        self._minerals = colony_data.minerals
        self._vespene = colony_data.vespene
        self._structures = colony_data.structures
        self._workers = colony_data.workers
        self._desired_vespene_workers = colony_data.desired_vespene_workers

    @property
    def id(self):
        return self._id

    @property
    def point(self):
        return self._point

    @property
    def is_starting_location(self):
        return self._is_starting_location

    @property
    def minerals(self):
        return self._minerals

    @property
    def vespene(self):
        return self._vespene

    @property
    def structures(self):
        return self._structures

    @structures.setter
    def structures(self, value):
        self._structures = value

    @property
    def workers(self):
        return self._workers

    @workers.setter
    def workers(self, value):
        self._workers = value

    @property
    def desired_vespene_workers(self):
        return self._desired_vespene_workers

    @desired_vespene_workers.setter
    def desired_vespene_workers(self, value):
        self._desired_vespene_workers = value
