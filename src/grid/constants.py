from enum import Enum

from grid.Position import Position

CELL_SIZE = 5
TILE_SIZE = 32

class Direction(Enum):
    NORTH = Position(0, -1)
    EAST = Position(-1, 0)
    SOUTH = Position(0, 1)
    WEST = Position(1, 0)
    NORTHEAST = Position(-1, -1)
    NORTHWEST = Position(1, -1)
    SOUTHEAST = Position(-1, 1)
    SOUTHWEST = Position(1, 1)

def findDirection(p0, p1):
    dx = p0.x - p1.x
    dy = p0.y - p1.y

    if dx == 0:
        return Direction.SOUTH if dy < 0 else Direction.NORTH
    elif dy == 0:
        return Direction.WEST if dx < 0 else Direction.EAST
    elif dx < 0:
        return Direction.SOUTHWEST if dy < 0 else Direction.NORTHWEST
    else:
        return Direction.SOUTHEAST if dy < 0 else Direction.NORTHEAST
