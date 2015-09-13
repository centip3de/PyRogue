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

        #print('building tiles. width is {0}. height is {0}'.format(self.width, self.height))

        for i in range(self.width):
            for j in range(self.height):
                realX = self.x * CELL_SIZE * TILE_SIZE + i * TILE_SIZE
                realY = self.y * CELL_SIZE * TILE_SIZE + j * TILE_SIZE

                self.tiles.append(
                    Tile(world, factory, 'bricks', realX, realY)
                )

# MAGIC
def buildMap(gridSize):
    cells = {}

    # fill some cells with rooms
    roomCount = min(10, gridSize * gridSize)
    for i in range(roomCount):
        x = random.randrange(0, gridSize)
        y = random.randrange(0, gridSize)

        while (x, y) in cells:
            x = random.randrange(0, gridSize)
            y = random.randrange(0, gridSize)

        #print('found empty spot at {0},{1}'.format(x,y))

        #width = random.randint(2, CELL_SIZE)
        #height = random.randint(2, CELL_SIZE)
        cells[(x, y)] = Room(x, y, CELL_SIZE, CELL_SIZE)#width, height)

    return list(cells.values())
