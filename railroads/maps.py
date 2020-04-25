
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
    pass


class StraightColumnHexmap(Hexmap):
    pass
