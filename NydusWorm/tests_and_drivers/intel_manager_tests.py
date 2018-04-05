import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
import sys
sys.path.insert(0,dir_path + "/../protocol")
sys.path.insert(0,dir_path + "/..")
import unittest
import IntelManager
import abathur_pb2
import score_pb2
import sc2api_pb2
import data_pb2
import raw_pb2
import common_pb2


def create_intel_response():
    intel = abathur_pb2.IntelResponse()
    intel.score.CopyFrom(score_pb2.Score())
    intel.resources.CopyFrom(sc2api_pb2.PlayerCommon())

    # Neutral
    geyser_1 = raw_pb2.Unit()
    geyser_1.display_type = 1
    geyser_1.alliance = 3
    geyser_1.tag = 4306239489
    geyser_1.unit_type = 342
    geyser_1.owner = 16
    geyser_1.pos.x = 117.5
    geyser_1.pos.y = 156.5
    geyser_1.pos.z = 11.984375

    geyser_1.facing = 471238
    geyser_1.radius = 1.5
    geyser_1.build_progress = 1
    geyser_1.cloak = 3
    geyser_1.is_on_screen = True
    geyser_1.health = 10000
    geyser_1.health_max = 10000
    geyser_1.vespene_contents = 2250

    mineralfield = raw_pb2.Unit()
    mineralfield.display_type = 1
    mineralfield.alliance = 3
    mineralfield.tag = 4306239489
    mineralfield.unit_type = 483
    mineralfield.owner = 16
    mineralfield.pos.x = 38
    mineralfield.pos.y = 46.5
    mineralfield.pos.x = 11.984375
    mineralfield.facing = 4.712389
    mineralfield.radius = 1.125
    mineralfield.build_progress = 1
    mineralfield.cloak = 3
    mineralfield.health = 10000
    mineralfield.health_max = 10000
    mineralfield.mineral_contents = 890

    rock6x6 = raw_pb2.Unit()
    rock6x6.display_type = raw_pb2.Snapshot
    rock6x6.alliance = 3
    rock6x6.tag = 8776253521
    rock6x6.unit_type = 371
    rock6x6.owner = 16
    rock6x6.pos.x = 108
    rock6x6.pos.y = 124
    rock6x6.pos.x = 8.957809
    rock6x6.facing = 7
    rock6x6.radius = 3.1875
    rock6x6.build_progress = 1
    rock6x6.cloak = 3

    # Self
    hatchery = raw_pb2.Unit()
    hatchery.display_type = 1
    hatchery.alliance = raw_pb2.Self
    hatchery.tag = 4336386049
    hatchery.unit_type = 86
    hatchery.owner = 1
    hatchery.pos.x = 37.5
    hatchery.pos.y = 53.5
    hatchery.pos.z = 11.984375
    hatchery.facing = 4.712389
    hatchery.radius = 2.75
    hatchery.build_progress = 1
    hatchery.cloak = 3
    hatchery.health = 1500
    hatchery.health_max = 1500
    hatchery.assigned_harvesters = 3
    hatchery.ideal_harvesters = 16

    spawning_pool = raw_pb2.Unit()
    spawning_pool.display_type = 1
    spawning_pool.alliance = 1
    spawning_pool.tag = 4345298945
    spawning_pool.unit_type = 89
    spawning_pool.owner = 1
    spawning_pool.pos.x = 31.5
    spawning_pool.pos.y = 52.5
    spawning_pool.pos.z = 11.984375
    spawning_pool.facing = 4.712389
    spawning_pool.radius = 1.8125
    spawning_pool.build_progress = 1
    spawning_pool.cloak = 3
    spawning_pool.health = 1000
    spawning_pool.health_max = 1000

    probe_1 = raw_pb2.Unit()
    probe_1.display_type = 1
    probe_1.alliance = 1
    probe_1.tag = 4338221057
    probe_1.unit_type = 84
    probe_1.owner = 1
    probe_1.pos.x = 122.369141
    probe_1.pos.y = 161.3877
    probe_1.pos.z = 11.984375
    probe_1.facing = 2.15306282
    probe_1.radius = 0.375
    probe_1.build_progress = 1
    probe_1.cloak = 3
    probe_1.is_on_screen = True
    probe_1.health = 20
    probe_1.health_max = 20
    probe_1.shield = 20

    probe_2 = raw_pb2.Unit()
    probe_2.display_type = 1
    probe_2.alliance = 1
    probe_2.tag = 4339269633
    probe_2.unit_type = 84
    probe_2.owner = 1
    probe_2.pos.x = 123.744141
    probe_2.pos.y = 161.505615
    probe_2.pos.z = 11.984375
    probe_2.facing = 1.76463509
    probe_2.radius = 0.375
    probe_2.build_progress = 1
    probe_2.cloak = 3
    probe_2.is_on_screen = True
    probe_2.health = 15.625
    probe_2.health_max = 20
    probe_2.buff_ids.extend([17])

    # Enemy
    factory = raw_pb2.Unit()
    factory.display_type = 1
    factory.alliance = 4
    factory.tag = 4349231107
    factory.unit_type = 27
    factory.owner = 2
    factory.pos.x = 128.5
    factory.pos.y = 153.5
    factory.pos.z = 11.984375
    factory.facing = 3.92529726
    factory.radius = 1.8125
    factory.build_progress = 0.198958337
    factory.cloak = 3
    factory.health = 349.015869
    factory.health_max = 1250

    marine = raw_pb2.Unit()
    marine.display_type = 1
    marine.alliance = 4
    marine.tag = 4337696770
    marine.unit_type = 48
    marine.owner = 2
    marine.pos.x = 125
    marine.pos.y = 153
    marine.pos.z = 11.984375
    marine.facing = 4.36424446
    marine.radius = 0.375
    marine.build_progress = 1
    marine.cloak = 3
    marine.health = 45
    marine.health_max = 45

    scv_1 = raw_pb2.Unit()
    scv_1.display_type = 1
    scv_1.alliance = 4
    scv_1.tag = 4341891073
    scv_1.unit_type = 45
    scv_1.owner = 2
    scv_1.pos.x = 127.375
    scv_1.pos.y = 154.625
    scv_1.pos.z = 11.984375
    scv_1.facing = 5.49754524
    scv_1.radius = 0.375
    scv_1.build_progress = 1
    scv_1.cloak = 3
    scv_1.health = 45
    scv_1.health_max = 45

    scv_2 = raw_pb2.Unit()
    scv_2.display_type = 1
    scv_2.alliance = 4
    scv_2.tag = 4343726081
    scv_2.unit_type = 45
    scv_2.owner = 2
    scv_2.pos.x = 124.103989
    scv_2.pos.y = 153.158936
    scv_2.pos.z = 11.984375
    scv_2.facing = 5.15599251
    scv_2.radius = 0.375
    scv_2.build_progress = 1
    scv_2.cloak = 3
    scv_2.health = 45
    scv_2.health_max = 45

    # Misc
    spawning_pool_type = data_pb2.UnitTypeData()
    spawning_pool_type.unit_id = 89
    spawning_pool_type.name = "SpawningPool"
    spawning_pool_type.available = True
    spawning_pool_type.attributes.extend([2, 3, 8]) # armored, biological and structure
    spawning_pool_type.armor = 1
    spawning_pool_type.mineral_cost = 250
    spawning_pool_type.ability_id = 1155
    spawning_pool_type.race = 2  # Zerg
    spawning_pool_type.build_time = 1040
    spawning_pool_type.tech_requirement = 86

    hatchery_type = data_pb2.UnitTypeData()
    hatchery_type.unit_id = 86
    hatchery_type.name = "Hatchery"
    hatchery_type.available = True
    hatchery_type.attributes.extend([data_pb2.Armored, data_pb2.Biological, data_pb2.Structure])
    hatchery_type.armor = 1
    hatchery_type.mineral_cost = 350
    hatchery_type.ability_id = 1152
    hatchery_type.race = common_pb2.Zerg
    hatchery_type.build_time = 1600
    hatchery_type.food_provided = 6

    build_spawning_pool = data_pb2.AbilityData()
    build_spawning_pool.ability_id = 1155
    build_spawning_pool.link_name = "ZergBuild"
    build_spawning_pool.link_index = 3
    build_spawning_pool.button_name = "SpawningPool"
    build_spawning_pool.friendly_name = "Build SpawningPool"
    build_spawning_pool.hotkey = "BS"
    build_spawning_pool.available = True
    build_spawning_pool.target = 2  # point
    build_spawning_pool.is_building = True
    build_spawning_pool.footprint_radius = 1.5

    psi_storm = data_pb2.BuffData()
    psi_storm.buff_id = 28
    psi_storm.name = "PsiStorm"

    ling_speed = data_pb2.UpgradeData()
    ling_speed.upgrade_id = 66
    ling_speed.name = "zerglingmovementspeed"
    ling_speed.mineral_cost = 100
    ling_speed.vespene_cost = 100
    ling_speed.research_time = 1760
    ling_speed.ability_id = 1253

    intel.alliedBuildings.extend([spawning_pool, hatchery])
    intel.alliedWorkers.extend([probe_1, probe_2])
    intel.alliedUnits.extend([probe_1, probe_2])
    intel.enemyVisibleBuildings.extend([factory])
    intel.enemyVisibleWorkers.extend([scv_1, scv_2])
    intel.enemyVisibleUnits.extend([marine])
    intel.mineralFields.extend([mineralfield])
    intel.vespeneGeysers.extend([geyser_1])
    intel.destructibles.extend([rock6x6])
    intel.abilities.extend([build_spawning_pool])
    intel.buffs.extend([psi_storm])
    intel.unitTypes.extend([spawning_pool_type, hatchery_type])
    intel.upgrades.extend([ling_speed])
    return intel


class Test_intel_manager_tests(unittest.TestCase):
    def test_update_given_intel_response_adds_repeated_data_with_multiple_elements_to_intel_manager(self):
        # Arrange
        intel = create_intel_response()
        man = IntelManager.IntelManager()
        # Act
        man.update_intel(intel)
        # Assert
        self.assertEqual(len(intel.alliedWorkers), len(man.allied_workers))
        self.assertEqual(len(intel.alliedUnits), len(man.allied_units))
        self.assertEqual(len(intel.enemyVisibleWorkers), len(man.enemy_visible_workers))
        self.assertEqual(len(intel.alliedBuildings), len(man.allied_buildings))

    def test_update_given_intel_response_adds_repeated_data_with_one_element_to_intel_manager(self):
        # Arrange
        intel = create_intel_response()
        man = IntelManager.IntelManager()
        # Act
        man.update_intel(intel)
        # Assert
        self.assertEqual(len(intel.enemyVisibleBuildings), len(man.enemy_visible_buildings))
        self.assertEqual(len(intel.enemyVisibleUnits), len(man.enemy_visible_units))
        self.assertEqual(len(intel.enemyVisibleUnits), len(man.enemy_visible_units))

    def test_update_given_intel_maps_spawningpool_ability_properly(self):
        # Arrange
        intel = create_intel_response()
        man = IntelManager.IntelManager()
        # Act
        man.update_intel(intel)
        # Assert
        self.assertNotEqual(None, man.ability_data[1155])

    def test_update_given_intel_maps_destructible_rock_properly(self):
        # Arrange
        intel = create_intel_response()
        man = IntelManager.IntelManager()
        # Act
        man.update_intel(intel)
        # Assert
        self.assertNotEqual(None, man.destructibles[8776253521])

    def test_update_given_intel_maps_psi_storm_buff_properly(self):
        # Arrange
        intel = create_intel_response()
        man = IntelManager.IntelManager()
        # Act
        man.update_intel(intel)
        # Assert
        self.assertNotEqual(None, man.buff_data[28])

    def test_update_given_intel_maps_ling_speed_upgrade_properly(self):
        # Arrange
        intel = create_intel_response()
        man = IntelManager.IntelManager()
        # Act
        man.update_intel(intel)
        # Assert
        self.assertNotEqual(None, man.upgrade_data[66])

    def test_update_given_intel_maps_minerals_properly(self):
        # Arrange
        intel = create_intel_response()
        man = IntelManager.IntelManager()
        # Act
        man.update_intel(intel)
        # Assert
        self.assertNotEqual(None, man.mineralfields[4306239489])

    def test_update_given_intel_maps_vespene_geysers_properly(self):
        # Arrange
        intel = create_intel_response()
        man = IntelManager.IntelManager()
        # Act
        man.update_intel(intel)
        # Assert
        self.assertNotEqual(None, man.vespene_geysers[4306239489])

    def test_update_given_intel_maps_spawning_pool_unit_properly(self):
        # Arrange
        intel = create_intel_response()
        man = IntelManager.IntelManager()
        # Act
        man.update_intel(intel)
        # Assert
        self.assertNotEqual(None, man.unit_data[89])

    def test_is_building_given_spawning_pool_returns_true(self):
        # Arrange
        intel = create_intel_response()
        man = IntelManager.IntelManager()
        man.update_intel(intel)
        # Act
        r = man.is_building(89)
        # Assert
        self.assertTrue(r)

    def test_isBuilding_given_probe_returns_false(self):
        # Arrange
        intel = create_intel_response()
        man = IntelManager.IntelManager()
        man.update_intel(intel)
        # Act
        r = man.is_building(84)
        # Assert
        self.assertFalse(r)

    def test_is_worker_given_probe_returns_true(self):
        # Arrange
        intel = create_intel_response()
        man = IntelManager.IntelManager()
        man.update_intel(intel)
        # Act
        r = man.is_worker(84)
        # Assert
        self.assertTrue(r)

    def test_is_worker_given_marine_returns_false(self):
        # Arrange
        intel = create_intel_response()
        man = IntelManager.IntelManager()
        man.update_intel(intel)
        # Act
        r = man.is_worker(48)
        # Assert
        self.assertFalse(r)

    def test_is_mineralfield_given_mineralfield_returns_true(self):
        # Arrange
        intel = create_intel_response()
        man = IntelManager.IntelManager()
        man.update_intel(intel)
        # Act
        r = man.is_mineralfield(483)
        # Assert
        self.assertTrue(r)

    def test_is_mineralfield_given_marine_returns_false(self):
        # Arrange
        intel = create_intel_response()
        man = IntelManager.IntelManager()
        man.update_intel(intel)
        # Act
        r = man.is_mineralfield(48)
        # Assert
        self.assertFalse(r)

    def test_is_vespene_geyser_given_vespene_geyser_returns_true(self):
        # Arrange
        intel = create_intel_response()
        man = IntelManager.IntelManager()
        man.update_intel(intel)
        # Act
        r = man.is_vespene_geyser(342)
        # Assert
        self.assertTrue(r)

    def test_is_vespene_geyser_given_mineralfield_returns_false(self):
        # Arrange
        intel = create_intel_response()
        man = IntelManager.IntelManager()
        man.update_intel(intel)
        # Act
        r = man.is_vespene_geyser(483)
        # Assert
        self.assertFalse(r)

    def test_is_destructible_given_destructible_rock_returns_true(self):
        # Arrange
        intel = create_intel_response()
        man = IntelManager.IntelManager()
        man.update_intel(intel)
        # Act
        r = man.is_destructible(371)
        # Assert
        self.assertTrue(r)

    def test_is_destructible_given_mineralfield_returns_false(self):
        # Arrange
        intel = create_intel_response()
        man = IntelManager.IntelManager()
        man.update_intel(intel)
        # Act
        r = man.is_destructible(483)
        # Assert
        self.assertFalse(r)

    def test_tech_requirements_full_given_spawning_pool_returns_list_with_hatchery(self):
        # Arrange
        intel = create_intel_response()
        man = IntelManager.IntelManager()
        man.update_intel(intel)
        # Act
        res = man.tech_requirements_full(89)
        # Assert
        self.assertTrue(man.get_unit_type_data(86) in res)

    def test_tech_requirements_given_spawning_pool_and_already_build_hatchery_returns_empty_list(self):
        # Arrange
        intel = create_intel_response()
        man = IntelManager.IntelManager()
        man.update_intel(intel)
        # Act
        res = man.tech_requirements(89)
        # Assert
        self.assertEqual([], res)


if __name__ == '__main__':
    unittest.main()
