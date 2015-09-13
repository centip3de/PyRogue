from grid.constants import *
from Tile import Tile

class Corridor:
    def __init__(self, room1, room2):
        self.room1 = room1
        self.room2 = room2

    def build(self, world, factory):
        tiles = []

        d = findDirection(self.room1.pos, self.room2.pos)

        startX = self.room1.pos[0] * CELL_SIZE * TILE_SIZE
        startY = self.room1.pos[1] * CELL_SIZE * TILE_SIZE

        endX = self.room2.pos[0] * CELL_SIZE * TILE_SIZE
        endY = self.room2.pos[1] * CELL_SIZE * TILE_SIZE

        if d.value[0] != 0:
            for x in range(startX, endX, d.value[0] * TILE_SIZE):
                tiles.append(Tile(world, factory, 'bricks', x, startY))

        if d.value[1] != 0:
            for y in range(startY, endY, d.value[1] * TILE_SIZE):
                tiles.append(Tile(world, factory, 'bricks', endX, y))

        return tiles
