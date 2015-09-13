import random

from Tile import Tile

TILE_SIZE = 32

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
                realX = self.x * TILE_SIZE + i * TILE_SIZE
                realY = self.y * TILE_SIZE + j * TILE_SIZE

                self.tiles.append(
                    Tile(world, factory, 'bricks', realX, realY)
                )

# MAGIC
def buildMap(cellSize, gridSize):
    cells = {}

    # fill some cells with rooms
    roomCount = 10
    for i in range(roomCount):
        x = random.randrange(0, gridSize) * cellSize
        y = random.randrange(0, gridSize) * cellSize

        while (x, y) in cells:
            x = random.randrange(0, gridSize) * cellSize
            y = random.randrange(0, gridSize) * cellSize

        width = random.randint(2, cellSize)
        height = random.randint(2, cellSize)
        cells[(x, y)] = Room(x, y, width, height)

    return cells.values()
