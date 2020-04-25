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
