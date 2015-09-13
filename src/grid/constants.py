from enum import Enum

CELL_SIZE = 5
TILE_SIZE = 32

class Direction(Enum):
    NORTH = (0, -1)
    EAST = (-1, 0)
    SOUTH = (0, 1)
    WEST = (1, 0)
    NORTHEAST = (-1, -1)
    NORTHWEST = (1, -1)
    SOUTHEAST = (-1, 1)
    SOUTHWEST = (1, 1)

def findDirection(p0, p1):
    dx = p0.x - p1.y
    dy = p0.x - p1.y

    if dx == 0:
        return Direction.SOUTH if dy < 0 else Direction.NORTH
    elif dy == 0:
        return Direction.WEST if dx < 0 else Direction.EAST
    elif dx < 0:
        return Direction.SOUTHWEST if dy < 0 else Direction.NORTHWEST
    else:
        return Direction.SOUTHEAST if dy < 0 else Direction.NORTHEAST
