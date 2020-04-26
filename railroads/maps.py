from enum import Enum

from amethyst.core import Object, Attr, dict_of


class Hexmap(Object):
    height = Attr(int)
    width = Attr(int)

    terrain = Attr(dict_of(int), default=dict)

    def _hexgrid_invariant(self, co):
        col, row = co
        if not (0 <= col <= self.width and 0 <= row <= self.height):
            return False
        return (col + row) & 1 == 0

    def __contains__(self, co):
        if not self._hexgrid_invariant(co):
            return False
        if self.terrain and co not in self.terrain:
            return False
        return True

    def register_terrain(self, data):
        terrain_types = Enum('Terrain', ' '.join(t.upper() for t in data))
        for t_name, coordinates in data.items():
            t = terrain_types[t_name.upper()]
            for co in coordinates:
                if not self._hexgrid_invariant(co):
                    continue
                self.terrain[co] = t


class StraightRowHexmap(Hexmap):
    def is_adjacent(self, co1, co2):
        if co1 not in self or co2 not in self:
            return False
        c, r = co1
        return any(
            (c + dc, r + dr) == co2 for dc, dr in [(2, 0), (1, -1), (-1, -1), (-2, 0), (-1, 1), (1, 1)]
        )


class StraightColumnHexmap(Hexmap):
    def is_adjacent(self, co1, co2):
        if co1 not in self or co2 not in self:
            return False
        c, r = co1
        return any(
            (c + dc, r + dr) == co2 for dc, dr in [(1, 1), (1, -1), (0, -2), (-1, -1), (-1, 1), (0, 2)]
        )
