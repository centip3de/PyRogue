from grid.Position import Position

import sdl2.ext

TILES = sdl2.ext.Resources(__file__, '../resources/tiles')

class Tile(sdl2.ext.Entity):
    def __init__(self, world, factory, name, x, y):
        self.sprite = factory.from_image(TILES.get_path(name + '.bmp'))
        self.position = Position(x, y)
        self.sprite.depth = 0
