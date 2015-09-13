import sdl2.ext

from movement import Velocity
from grid.Position import Position

class Player(sdl2.ext.Entity):
    def __init__(self, world, sprite, x, y):
        self.sprite             = sprite
        self.position           = Position(x, y)
        self.sprite.depth       = 1
        self.playerdata         = PlayerData()

    def walk(self, grid, direction):
        x = self.position.x + direction.value.x
        y = self.position.y + direction.value.y

        if grid.hasTileAt(x, y):
            self.position = Position(x, y)

class PlayerData(object):
    def __init__(self):
        super(PlayerData, self).__init__()
        self.inventory  = []
        self.health     = 50
        self.equipped   = {}
