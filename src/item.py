import sdl2.ext
from enum import Enum

# Item entity. The actual renderable portion of an item.
class Item(sdl2.ext.Entity):
    def __init__(self, world, sprite, x, y, type, data):
        self.sprite             = sprite
        self.sprite.position    = (x, y)
        self.sprite.depth       = 1
        self.data               = Data(type, data)

# Data container for any renderable object (excluding the player)
class Data(object):
    def __init__(self, type, data):
        super(Data, self).__init__()
        self.type = type 
        self.data = data 

# Enum of types for the Data container
class DataTypes(Enum):
    ITEM        = 1
    WEAPON      = 2
    UNPATHABLE  = 3
    PATHABLE    = 4
    CONSUMABLE  = 5
