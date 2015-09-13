from grid.constants import *
from entities.Tile import Tile

class Corridor:
    def __init__(self, room1, room2):
        self.room1 = room1
        self.room2 = room2

    def build(self, world, factory):
        tiles = []

        d = findDirection(self.room1.pos, self.room2.pos)

        startX = self.room1.pos.x
        startY = self.room1.pos.y

        endX = self.room2.pos.x
        endY = self.room2.pos.y

        if d.value.x != 0:
            for x in range(startX, endX, d.value.x):
                tiles.append(Tile(world, factory, 'bricks', x, startY))

        if d.value.y != 0:
            for y in range(startY, endY, d.value.y):
                tiles.append(Tile(world, factory, 'bricks', endX, y))

        return tiles
