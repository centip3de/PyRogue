import random
import math

from Tile import Tile

from grid.constants import *
from grid.Grid import *
from grid.Room import *
from grid.Corridor import *

def safeToPlace(cells, coord):
    x = coord[0]
    y = coord[1]

    return \
        (x - 1, y) not in cells and \
        (x + 1, y) not in cells and \
        (x, y - 1) not in cells and \
        (x, y + 1) not in cells

def findNearestNeighbor(cells, coord):
    def dist2(c):
        d = math.sqrt((c[0] - coord[0]) ** 2 + (c[1] - coord[1]) ** 2)
        if d == 0:
            return float('inf')
        else:
            return d

    coord1 = sorted(cells.keys(), key = dist2)[0]
    return cells[coord1]

def buildMap(gridSize):
    cells = {}

    # generate a list of candidate coords for cells
    roomCoords = [(x, y) for x in range(gridSize) for y in range(gridSize)]
    random.shuffle(roomCoords)

    roomCount = min(10, int(gridSize * gridSize / 2))
    for i in range(roomCount):
        if len(roomCoords) == 0:
            break

        # search for candidate cell
        coord = roomCoords.pop()

        while not safeToPlace(cells, coord) and len(roomCoords) > 0:
            coord = roomCoords.pop()

        if not safeToPlace(cells, coord):
            break

        width = random.randint(3, CELL_SIZE)
        height = random.randint(3, CELL_SIZE)
        cells[coord] = Room(coord[0], coord[1], width, height)

    grid = Grid()
    grid.rooms = list(cells.values())

    # connect every room to one neighbor
    for coord in cells:
        room = cells[coord]
        room1 = findNearestNeighbor(cells, coord)

        if not grid.connected(room, room1):
            grid.corridors.append(Corridor(room, room1))

    return grid
