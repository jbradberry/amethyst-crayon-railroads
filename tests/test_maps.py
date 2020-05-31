import unittest

from railroads import engine, maps


class HexmapContainerRowTest(unittest.TestCase):
    def setUp(self):
        self.game = engine.RailroadEngine()
        data = [('default', 'row', 5, 5)]
        self.game.map_load_definition(data)

        plains = [(c, r) for r in range(3) for c in range(5)]
        mountains = [(c, r) for r in range(3, 5) for c in range(5)]
        data = {'plain': {'default': plains}, 'mountain': {'default': mountains}}
        self.game.map_load_hexes(data)

    def test_in_bounds(self):
        for r in range(5):
            for c in range(r & 1, 5, 2):
                self.assertTrue(self.game.map_contains(('default', c, r)))

    def test_wrong_phase(self):
        for r in range(5):
            for c in range((r + 1) & 1, 5, 2):
                self.assertFalse(self.game.map_contains(('default', c, r)))

    def test_out_of_bounds(self):
        self.assertFalse(self.game.map_contains(('default', -1, 5)))
        self.assertFalse(self.game.map_contains(('default', 3, -1)))
        self.assertFalse(self.game.map_contains(('default', 6, 4)))
        self.assertFalse(self.game.map_contains(('default', 2, 12)))

    def test_is_adjacent(self):
        for col, row in [(1, 1), (3, 1), (0, 2), (4, 2), (1, 3), (3, 3)]:
            self.assertTrue(
                self.game.map_is_adjacent(('default', 2, 2), ('default', col, row)),
                f"('default', {col}, {row}) is not adjacent to ('default', 2, 2)."
            )

    def test_not_adjacent_off_the_edge(self):
        self.assertFalse(self.game.map_is_adjacent(('default', 4, 0), ('default', 6, 0)))

    def test_not_adjacent_too_far(self):
        self.assertFalse(self.game.map_is_adjacent(('default', 1, 3), ('default', 3, 1)))

    def test_not_adjacent_wrong_phase(self):
        self.assertFalse(self.game.map_is_adjacent(('default', 3, 3), ('default', 4, 3)))

    def test_adjacent_list_middle(self):
        self.assertCountEqual(
            self.game.map_adjacent(('default', 2, 2)),
            [('default', 1, 1), ('default', 3, 1), ('default', 0, 2),
             ('default', 4, 2), ('default', 1, 3), ('default', 3, 3)]
        )

    def test_adjacent_list_edge(self):
        self.assertCountEqual(
            self.game.map_adjacent(('default', 4, 2)),
            [('default', 3, 1), ('default', 2, 2), ('default', 3, 3)]
        )

    def test_adjacent_list_out_of_bounds(self):
        self.assertCountEqual(self.game.map_adjacent(('default', 5, 5)), [])

    def test_adjacent_list_wrong_phase(self):
        self.assertCountEqual(self.game.map_adjacent(('default', 3, 2)), [])

#     def test_terrain(self):
#         terrain = type(_map.hexes[(0, 0)].terrain)
#         self.assertEqual(len(_map.hexes), 13)
#         self.assertEqual(sum(1 for co, H in _map.hexes.items() if H.terrain == terrain.PLAIN), 8)
#         self.assertEqual(sum(1 for co, H in _map.hexes.items() if H.terrain == terrain.MOUNTAIN), 5)


class HexmapContainerColumnTest(unittest.TestCase):
    def setUp(self):
        self.game = engine.RailroadEngine()
        data = [('default', 'column', 5, 5)]
        self.game.map_load_definition(data)

        plains = [(c, r) for r in range(3) for c in range(5)]
        mountains = [(c, r) for r in range(3, 5) for c in range(5)]
        data = {'plain': {'default': plains}, 'mountain': {'default': mountains}}
        self.game.map_load_hexes(data)

    def test_in_bounds(self):
        for c in range(5):
            for r in range(c & 1, 5, 2):
                self.assertTrue(self.game.map_contains(('default', c, r)))

    def test_wrong_phase(self):
        for c in range(5):
            for r in range((c + 1) & 1, 5, 2):
                self.assertFalse(self.game.map_contains(('default', c, r)))

    def test_out_of_bounds(self):
        self.assertFalse(self.game.map_contains(('default', -1, 5)))
        self.assertFalse(self.game.map_contains(('default', 3, -1)))
        self.assertFalse(self.game.map_contains(('default', 6, 4)))
        self.assertFalse(self.game.map_contains(('default', 2, 12)))

    def test_is_adjacent(self):
        for col, row in [(1, 1), (1, 3), (2, 0), (2, 4), (3, 1), (3, 3)]:
            self.assertTrue(
                self.game.map_is_adjacent(('default', 2, 2), ('default', col, row)),
                f"('default', {col}, {row}) is not adjacent to ('default', 2, 2)."
            )

    def test_not_adjacent_off_the_edge(self):
        self.assertFalse(self.game.map_is_adjacent(('default', 4, 4), ('default', 5, 5)))

    def test_not_adjacent_too_far(self):
        self.assertFalse(self.game.map_is_adjacent(('default', 1, 3), ('default', 3, 1)))

    def test_not_adjacent_wrong_phase(self):
        self.assertFalse(self.game.map_is_adjacent(('default', 3, 3), ('default', 4, 3)))

    def test_adjacent_list_middle(self):
        self.assertCountEqual(
            self.game.map_adjacent(('default', 2, 2)),
            [('default', 1, 1), ('default', 1, 3), ('default', 2, 0),
             ('default', 2, 4), ('default', 3, 1), ('default', 3, 3)]
        )

    def test_adjacent_list_edge(self):
        self.assertCountEqual(
            self.game.map_adjacent(('default', 4, 2)),
            [('default', 3, 1), ('default', 3, 3), ('default', 4, 0), ('default', 4, 4)]
        )

    def test_adjacent_list_out_of_bounds(self):
        self.assertCountEqual(self.game.map_adjacent(('default', 5, 5)), [])

    def test_adjacent_list_wrong_phase(self):
        self.assertCountEqual(self.game.map_adjacent(('default', 3, 2)), [])

#     def test_terrain(self):
#         terrain = type(_map.hexes[(0, 0)].terrain)
#         self.assertEqual(len(_map.hexes), 13)
#         self.assertEqual(sum(1 for co, H in _map.hexes.items() if H.terrain == terrain.PLAIN), 8)
#         self.assertEqual(sum(1 for co, H in _map.hexes.items() if H.terrain == terrain.MOUNTAIN), 5)


if __name__ == '__main__':
    unittest.main()
