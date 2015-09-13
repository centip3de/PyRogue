from Tile import Tile
from grid.constants import *

class Room:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def build(self, world, factory):
        def tile(i, j):
            realX = self.x * CELL_SIZE * TILE_SIZE + i * TILE_SIZE
            realY = self.y * CELL_SIZE * TILE_SIZE + j * TILE_SIZE
            return Tile(world, factory, 'bricks', realX, realY)

        return [tile(i, j) for i in range(self.width) for j in range(self.height)]
