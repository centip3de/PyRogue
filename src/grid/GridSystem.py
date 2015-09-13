from grid.constants import TILE_SIZE

import sdl2.ext
import math

class Position(object):
    def __init__(self, x, y):
        super(Position, self).__init__()
        self.x = x
        self.y = y

class GridSystem(sdl2.ext.Applicator):
    def __init__(self, width, height, player):
        super(GridSystem, self).__init__()

        self.componenttypes = (Position, sdl2.ext.Sprite)
        self.centerX = math.floor((width / TILE_SIZE) / 2)
        self.centerY = math.floor((height / TILE_SIZE) / 2)
        self.player = player

    def process(self, world, componentsets):
        playerPos = self.player.position

        for position, sprite in componentsets:
            realX = (position.x - playerPos.x + self.centerX) * TILE_SIZE
            realY = (position.y - playerPos.y + self.centerY) * TILE_SIZE

            sprite.position = realX, realY
