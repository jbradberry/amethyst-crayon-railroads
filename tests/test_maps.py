import unittest

from railroads import maps


class StraightRowHexmapTest(unittest.TestCase):
    def setUp(self):
        self.map = maps.StraightRowHexmap(width=8, height=8)

    def test_in_bounds(self):
        for r in range(8):
            for c in range(r & 1, 8, 2):
                self.assertIn((c, r), self.map)

    def test_wrong_phase(self):
        for r in range(8):
            for c in range((r + 1) & 1, 8, 2):
                self.assertNotIn((c, r), self.map)

    def test_out_of_bounds(self):
        self.assertNotIn((-1, 5), self.map)
        self.assertNotIn((3, -1), self.map)
        self.assertNotIn((10, 6), self.map)
        self.assertNotIn((2, 12), self.map)

    def test_is_adjacent(self):
        for co in [(3, 3), (5, 3), (2, 4), (6, 4), (3, 5), (5, 5)]:
            self.assertTrue(self.map.is_adjacent((4, 4), co))

    def test_not_adjacent_off_the_edge(self):
        self.assertFalse(self.map.is_adjacent((6, 0), (7, -1)))

    def test_not_adjacent_too_far(self):
        self.assertFalse(self.map.is_adjacent((5, 3), (7, 1)))

    def test_not_adjacent_wrong_phase(self):
        self.assertFalse(self.map.is_adjacent((3, 3), (4, 3)))

    def test_terrain(self):
        _map = maps.StraightRowHexmap(width=5, height=5)
        plains = [(c, r) for r in range(3) for c in range(5)]
        mountains = [(c, r) for r in range(3, 5) for c in range(5)]
        data = {'plain': plains, 'mountain': mountains}
        _map.register_hexes(data)
        terrain = type(_map.hexes[(0, 0)].terrain)

        self.assertEqual(len(_map.hexes), 13)
        self.assertEqual(sum(1 for co, H in _map.hexes.items() if H.terrain == terrain.PLAIN), 8)
        self.assertEqual(sum(1 for co, H in _map.hexes.items() if H.terrain == terrain.MOUNTAIN), 5)


class StraightColumnHexmapTest(unittest.TestCase):
    def setUp(self):
        self.map = maps.StraightColumnHexmap(width=8, height=8)

    def test_in_bounds(self):
        for c in range(8):
            for r in range(c & 1, 8, 2):
                self.assertIn((c, r), self.map)

    def test_wrong_phase(self):
        for c in range(8):
            for r in range((c + 1) & 1, 8, 2):
                self.assertNotIn((c, r), self.map)

    def test_out_of_bounds(self):
        self.assertNotIn((-1, 5), self.map)
        self.assertNotIn((3, -1), self.map)
        self.assertNotIn((10, 6), self.map)
        self.assertNotIn((2, 12), self.map)

    def test_is_adjacent(self):
        for co in [(3, 3), (3, 5), (4, 2), (4, 6), (5, 3), (5, 5)]:
            self.assertTrue(self.map.is_adjacent((4, 4), co))

    def test_not_adjacent_off_the_edge(self):
        self.assertFalse(self.map.is_adjacent((6, 0), (5, -1)))

    def test_not_adjacent_too_far(self):
        self.assertFalse(self.map.is_adjacent((5, 3), (7, 1)))

    def test_not_adjacent_wrong_phase(self):
        self.assertFalse(self.map.is_adjacent((3, 3), (4, 3)))

    def test_terrain(self):
        _map = maps.StraightRowHexmap(width=5, height=5)
        plains = [(c, r) for r in range(3) for c in range(5)]
        mountains = [(c, r) for r in range(3, 5) for c in range(5)]
        data = {'plain': plains, 'mountain': mountains}
        _map.register_hexes(data)
        terrain = type(_map.hexes[(0, 0)].terrain)

        self.assertEqual(len(_map.hexes), 13)
        self.assertEqual(sum(1 for co, H in _map.hexes.items() if H.terrain == terrain.PLAIN), 8)
        self.assertEqual(sum(1 for co, H in _map.hexes.items() if H.terrain == terrain.MOUNTAIN), 5)
