import sdl2.ext
from components.Velocity import Velocity

# Handles the movement of all entities
class MovementSystem(sdl2.ext.Applicator):
    def __init__(self, minx, miny, maxx, maxy):
        super(MovementSystem, self).__init__()

        self.componenttypes = (Velocity, sdl2.ext.Sprite)
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy

    # Moves the sprites according to their velocity, forcing them to stay on screen
    def process(self, world, componentsets):
        for velocity, sprite in componentsets:

            swidth, sheight = sprite.size
            sprite.x += velocity.vx
            sprite.y += velocity.vy

            sprite.x = max(self.minx, sprite.x)
            sprite.y = max(self.miny, sprite.y)

            pmaxx = sprite.x + swidth
            pmaxy = sprite.y + sheight

            if(pmaxx > self.maxx):
                sprite.x = self.maxx - swidth
            if(pmaxy > self.maxy):
                sprite.y = self.maxy - sheight
