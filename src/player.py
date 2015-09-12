import sdl2.ext

class Player(sdl2.ext.Entity):
    def __init__(self, world, sprite, x=0, y=0):
        self.sprite = sprite
        self.sprite.position = (x,y)
