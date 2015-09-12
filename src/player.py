import sdl2.ext
from movement import Velocity

class Player(sdl2.ext.Entity):
    def __init__(self, world, sprite, x, y):
        self.sprite             = sprite
        self.sprite.position    = (x, y)
        self.sprite.depth       = 1
        self.velocity           = Velocity()
