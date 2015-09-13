import sdl2.ext

class Item(sdl2.ext.Entity):
    def __init__(self, world, sprite, x, y, data):
        self.sprite             = sprite
        self.sprite.position    = (x, y)
        self.sprite.depth       = 1
        self.data               = Data("Item", data)

class Data(object):
    def __init__(self, type, data):
        super(Data, self).__init__()
        self.type = type
        self.data = data 
