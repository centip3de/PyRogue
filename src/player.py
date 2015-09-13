import sdl2.ext

from movement import Velocity
from grid.GridSystem import Position

class Player(sdl2.ext.Entity):
    def __init__(self, world, sprite, x, y):
        self.sprite             = sprite
        self.position           = Position(x, y)
        self.sprite.depth       = 1
        self.playerdata         = PlayerData()

class PlayerData(object):
    def __init__(self):
        super(PlayerData, self).__init__()
        self.inventory  = []
        self.health     = 50
        self.equipped   = {}
