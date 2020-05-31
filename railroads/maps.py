from enum import Enum

from amethyst.core import Object, Attr, dict_of
from amethyst.games import EnginePlugin


DIRECTIONS = {
    'row': [(2, 0), (1, -1), (-1, -1), (-2, 0), (-1, 1), (1, 1)],
    'column': [(1, 1), (1, -1), (0, -2), (-1, -1), (-1, 1), (0, 2)],
}


class HexmapContainer(EnginePlugin):
    AMETHYST_PLUGIN_COMPAT = 1  # Plugin API version
    AMETHYST_ENGINE_METHODS = [
        'load_definition', 'load_hexes',
        'contains', 'is_adjacent', 'adjacent'
    ]
    AMETHYST_ENGINE_DEFAULT_METHOD_PREFIX = "map_"

    _maps = Attr(default=dict)
    _terrain = Attr(default=dict)

    def hexgrid_invariant(self, map_name, col, row):
        if map_name not in self._maps:
            return False
        _, height, width = self._maps[map_name]

        if not (0 <= col <= width and 0 <= row <= height):
            return False
        return (col + row) & 1 == 0

    def load_definition(self, game, data):
        for name, _type, height, width in data:
            if _type not in DIRECTIONS:
                continue
            self._maps[name] = (_type, height, width)

    def load_hexes(self, game, data):
        terrain_types = Enum('Terrain', ' '.join(t.upper() for t in data))
        for t_name, maps in data.items():
            t = terrain_types[t_name.upper()]
            for map_name, coordinates in maps.items():
                for col, row in coordinates:
                    if not self.hexgrid_invariant(map_name, col, row):
                        continue
                    self._terrain[(map_name, col, row)] = t

    def contains(self, game, coordinates):
        if not self.hexgrid_invariant(*coordinates):
            return False
        return coordinates in self._terrain

    def is_adjacent(self, game, co1, co2):
        if co1[0] != co2[0]:
            return False
        if not self.contains(game, co1) or not self.contains(game, co2):
            return False
        map_name, col, row = co1
        return any(
            (map_name, col + dc, row + dr) == co2
            for dc, dr in DIRECTIONS[self._maps[map_name][0]]
        )

    def adjacent(self, game, coordinates):
        if not self.contains(game, coordinates):
            return []
        map_name, col, row = coordinates
        return [
            (map_name, col + dc, row + dr)
            for dc, dr in DIRECTIONS[self._maps[map_name][0]]
            if self.contains(game, (map_name, col + dc, row + dr))
        ]
