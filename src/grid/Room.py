import random

from Tile import Tile
from grid.Position import Position
from grid.constants import *

class Room:
    def __init__(self, x, y, width, height):
        self.pos = Position(x, y)
        self.width = width
        self.height = height

    def build(self, world, factory):
        def tile(i, j):
            realX = self.pos.x * CELL_SIZE + i
            realY = self.pos.y * CELL_SIZE + j
            return Tile(world, factory, 'bricks', realX, realY)

        return [tile(i, j) for i in range(self.width) for j in range(self.height)]
