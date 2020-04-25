
from amethyst.core  import Object, Attr


class Hexmap(Object):
    height = Attr()
    width = Attr()

    def __contains__(self, coordinates):
        col, row = coordinates
        if not (0 <= col <= self.width and 0 <= row <= self.height):
            return False
        return (col + row) & 1 == 0


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
