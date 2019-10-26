import unittest
from mapping import Map
from update import TileUpdate


class MapTest(unittest.TestCase):

    def test_enemy_base(self):
        map = Map()
        self.assertFalse(map.enemy_base_found())
        map.update_tiles([
            TileUpdate({"x": 0, "y": 0, "units": [{"type": "base"}]})
        ])
        self.assertTrue(map.enemy_base_found())


if __name__ == '__main__':
    unittest.main()