import random

from Tile import Tile

TILE_SIZE = 32
CELL_SIZE = 5

# MAGIC
class Room:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def buildTiles(self, world, factory):
        self.tiles = []

        for i in range(self.width):
            for j in range(self.height):
                realX = self.x * CELL_SIZE * TILE_SIZE + i * TILE_SIZE
                realY = self.y * CELL_SIZE * TILE_SIZE + j * TILE_SIZE

                self.tiles.append(
                    Tile(world, factory, 'bricks', realX, realY)
                )

# MAGIC
def safeToPlace(cells, coord):
    x = coord[0]
    y = coord[1]

    return \
        (x - 1, y) not in cells and \
        (x + 1, y) not in cells and \
        (x, y - 1) not in cells and \
        (x, y + 1) not in cells

def buildMap(gridSize):
    cells = {}

    # generate a list of candidate coords for cells
    roomCoords = [(x, y) for x in range(gridSize) for y in range(gridSize)]
    random.shuffle(roomCoords)

    roomCount = min(10, gridSize * gridSize / 2)
    for i in range(roomCount):
        # search for candidate cell
        coord = roomCoords.pop()

        while not safeToPlace(cells, coord) and len(roomCoords) > 0:
            coord = roomCoords.pop()

        if not safeToPlace(cells, coord):
            break

        width = random.randint(3, CELL_SIZE)
        height = random.randint(3, CELL_SIZE)
        cells[coord] = Room(coord[0], coord[1], width, height)

    return list(cells.values())
