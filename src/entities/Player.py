import sdl2.ext

from components.Velocity import Velocity
from entities.PlayerData import PlayerData
from components.Position import Position

class Player(sdl2.ext.Entity):
    def __init__(self, world, sprite, x, y):
        self.sprite             = sprite
        self.position           = Position(x, y)
        self.sprite.depth       = 2
        self.playerdata         = PlayerData()

    def walk(self, grid, direction):
        x = self.position.x + direction.value.x
        y = self.position.y + direction.value.y

        if grid.hasTileAt(x, y):
            self.position = Position(x, y)
