import sdl2.ext
from enum import Enum

from components.Position import Position
ITEMS = sdl2.ext.Resources(__file__, '../../resources/items')

# Item entity. The actual renderable portion of an item.
class Item(sdl2.ext.Entity):
    def __init__(self, world, factory, name, x, y, type, data):
        self.sprite = factory.from_image(ITEMS.get_path(name + '.png'))
        self.position           = Position(x, y)
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

# Enum of types of weapons
class WeaponTypes(Enum):
    BOW         = 1
    SWORD       = 2
    AXE         = 3
    STICK       = 4
    DAGGER      = 5
    CLUB        = 6
    FLAIL       = 7
    SPEAR       = 8
    SLING       = 9
    CROSSBOW    = 10

# Enum of types of consumables
class ConsumableTypes(Enum):
    HEALTH_POT  = 1
    MANA_POT    = 2

# Enum of types of items
class ItemTypes(Enum):
    KEY         = 1
    LAMP        = 2
