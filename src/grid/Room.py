import random

from entities.Tile import Tile
from entities.Item import Item, DataTypes
from components.Position import Position
from grid.constants import *

class Room:
    def __init__(self, world, factory, x, y, width, height):
        self.pos = Position(x, y)
        self.width = width
        self.height = height
        self.items = []

        if random.random() < 0.33:
            itemX = random.randint(x, x + width - 1)
            itemY = random.randint(y, y + height - 1)

            self.items.append(
                Item(world, factory, 'sandwich', itemX, itemY, DataTypes.ITEM, 'Sandwich')
            )

    def build(self, world, factory):
        def tile(i, j):
            realX = self.pos.x + i
            realY = self.pos.y + j
            return Tile(world, factory, 'bricks', realX, realY)

        return [tile(i, j) for i in range(self.width) for j in range(self.height)] + self.items
