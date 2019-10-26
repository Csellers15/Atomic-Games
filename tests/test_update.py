import unittest

from update import UnitInfo, GameInfo, ResourceUpdate, TileUpdate, UnitUpdate, GameUpdate


class UnitInfoTest(unittest.TestCase):

    def test_all_unit_info_fields(self):
        data = {
            "attack_cooldown_duration": 30,
            "attack_damage": 1,
            "attack_type": "melee",
            "can_carry": True,
            "cost": 130,
            "create_time": 100,
            "hp": 5,
            "range": 5,
            "speed": 3
        }
        update = UnitInfo(data)
        self.assertEqual(update.hp, 5)
        self.assertEqual(update.range, 5)
        self.assertEqual(update.cost, 130)
        self.assertEqual(update.speed, 3)
        self.assertEqual(update.attack_damage, 1)
        self.assertEqual(update.attack_type, "melee")
        self.assertEqual(update.attack_cooldown_duration, 30)
        self.assertEqual(update.can_carry, True)
        self.assertEqual(update.create_time, 100)

    def test_unit_info_with_fields_missing(self):
        data = {
            "cost": 10,
            "hp": 50,
            "range": 2,
            "speed": 1
        }
        update = UnitInfo(data)
        self.assertEqual(update.hp, 50)
        self.assertEqual(update.range, 2)
        self.assertEqual(update.cost, 10)
        self.assertEqual(update.speed, 1)
        self.assertIsNone(update.attack_damage)
        self.assertIsNone(update.attack_type)
        self.assertIsNone(update.attack_cooldown_duration)
        self.assertIsNone(update.can_carry)
        self.assertIsNone(update.create_time)


class GameInfoTest(unittest.TestCase):
    def test_game_info(self):
        data = {
            "game_duration": 30,
            "map_height": 32,
            "map_width": 32,
            "turn_duration": 200,
            "unit_info": {
                "base": {
                    "hp": 30,
                },
                "scout": {
                    "hp": 20,
                }
            }
        }
        info = GameInfo(data)
        self.assertEqual(info.game_duration, 30)
        self.assertEqual(info.map_height, 32)
        self.assertEqual(info.map_width, 32)
        self.assertEqual(info.turn_duration, 200)
        self.assertEqual(info.unit_info.base.hp, 30)
        self.assertEqual(info.unit_info.scout.hp, 20)
        self.assertIsNone(info.unit_info.tank)


class ResourceUpdateTest(unittest.TestCase):
    def test_fields(self):
        data = {
            "id": 1,
            "type": "small",
            "total": 2,
            "value": 3
        }
        update = ResourceUpdate(data)
        self.assertEqual(update.id, 1)
        self.assertEqual(update.type, "small")
        self.assertEqual(update.total, 2)
        self.assertEqual(update.value, 3)


class TileUpdateTest(unittest.TestCase):
    def test_fields(self):
        data = {
            "blocked": False,
            "visible": True,
            "resources": {"id": 1},
            "units": [{"id": 2}, {"id": 3}],
            "x": -2,
            "y": 4
        }
        update = TileUpdate(data)
        self.assertFalse(update.blocked)
        self.assertTrue(update.visible)
        self.assertEqual(update.x, -2)
        self.assertEqual(update.y, 4)
        self.assertEqual(update.resource.id, 1)
        self.assertEqual(update.units[0].id, 2)
        self.assertEqual(update.units[1].id, 3)


class UnitUpdateTest(unittest.TestCase):
    def test_fields(self):
        data = {
            "attack_cooldown": 0,
            "attack_cooldown_duration": 30,
            "attack_damage": 2,
            "attack_type": "melee",
            "can_attack": True,
            "health": 10,
            "id": 6,
            "player_id": 0,
            "range": 2,
            "resource": 0,
            "speed": 5,
            "status": "idle",
            "type": "worker",
            "x": 0,
            "y": 0
        }
        update = UnitUpdate(data)
        self.assertEqual(update.attack_cooldown, 0)
        self.assertEqual(update.attack_cooldown_duration, 30)
        self.assertEqual(update.attack_damage, 2)
        self.assertEqual(update.attack_type, "melee")
        self.assertEqual(update.can_attack, True)
        self.assertEqual(update.health, 10)
        self.assertEqual(update.id, 6)
        self.assertEqual(update.player_id, 0)
        self.assertEqual(update.range, 2)
        self.assertEqual(update.resource, 0)
        self.assertEqual(update.speed, 5)
        self.assertEqual(update.status, "idle")
        self.assertEqual(update.type, "worker")
        self.assertEqual(update.x, 0)
        self.assertEqual(update.y, 0)


class GameUpdateTest(unittest.TestCase):
    def test_fields(self):
        data = {
            "player": 0,
            "time": 1,
            "turn": 2,
            "game_info": {
                "map_height": 32,
                "map_width": 32,
            },
            "tile_updates": [
                {
                    "x": -2,
                    "y": -2
                }],
            "unit_updates": [
                {
                    "x": 0,
                    "y": 0
                }]
        }
        update = GameUpdate(data)
        self.assertEqual(update.player, 0)
        self.assertEqual(update.time, 1)
        self.assertEqual(update.turn, 2)
        self.assertEqual(update.game_info.map_width, 32)
        self.assertEqual(update.tile_updates[0].x, -2)
        self.assertEqual(update.unit_updates[0].y, 0)



if __name__ == '__main__':
    unittest.main()
