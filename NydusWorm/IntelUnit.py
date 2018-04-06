import os
dir_path = os.path.dirname(os.path.realpath(__file__))
import sys
sys.path.insert(0, dir_path + "/protocol")

import raw_pb2


class IntelUnit:
    """Class wrapping a protobuf Unit to allow for automatic update and the addition of
       the last_seen attribute"""
    def __init__(self, unit, last_seen):
        self.unit = unit
        self.last_seen = last_seen

    def set_unit(self, unit, last_seen):
        """Internal method do not use"""
        self.unit = unit
        self.last_seen = last_seen

    def addon_tag(self):
        return self.unit.addon_tag

    def frames_since_seen(self, current_loop):
        return current_loop - self.last_seen

    def alliance(self):
        return self.unit.alliance

    def assigned_harvesters(self):
        return self.unit.assigned_harvesters

    def buff_ids(self):
        return self.unit.buff_ids

    def build_progress(self):
        return self.unit.build_progress

    def cargo_space_max(self):
        return self.unit.cargo_space_max

    def cargo_space_taken(self):
        return self.unit.cargo_space_taken

    def cloak(self):
        return self.unit.cloak

    def detect_range(self):
        return self.unit.detect_range

    def display_type(self):
        if self.frames_since_seen() is 0:
            return self.unit.display_type
        return raw_pb2.Snapshot

    def energy(self):
        return self.unit.energy

    def engaged_target_tag(self):
        return self.unit.engaged_target_tag

    def facing(self):
        return self.unit.facing

    def health_max(self):
        return self.unit.health_max

    def ideal_harvesters(self):
        return self.unit.ideal_harvesters

    def is_blip(self):
        return self.unit.is_blip

    def is_burrowed(self):
        return self.unit.is_burrowed

    def is_flying(self):
        return self.unit.is_flying

    def is_on_screen(self):
        return self.unit.is_on_screen

    def is_powered(self):
        return self.unit.is_powered

    def is_selected(self):
        return self.unit.is_selected

    def mineral_contents(self):
        return self.unit.mineral_contents

    def orders(self):
        return self.unit.orders

    def owner(self):
        return self.unit.owner

    def passengers(self):
        return self.unit.passengers

    def pos(self):
        return self.unit.pos

    def radar_ranger(self):
        return self.unit.radar_range

    def radius(self):
        return self.unit.radius

    def shield(self):
        return self.unit.shield

    def tag(self):
        return self.unit.tag

    def unit_type(self):
        return self.unit.unit_type

    def vespene_contents(self):
        return self.unit.vespene_contents

    def weapon_cooldown(self):
        return self.unit.weapon_cooldown

    def __eq__(self, other):
        return isinstance(other, IntelUnit) and other.tag() == self.tag()

    def __hash__(self):
        return self.tag()