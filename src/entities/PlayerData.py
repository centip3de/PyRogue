from enum import Enum

class PlayerData(object):
    def __init__(self):
        super(PlayerData, self).__init__()
        self.health                             = 50
        self.equipped                           = {}
        self.equipped[Equippable.WEAPON]        = None
        self.equipped[Equippable.CONSUMABLE]    = None
        self.equipped[Equippable.ITEM]          = None

class Equippable(Enum):
    WEAPON      = 1
    CONSUMABLE  = 2
    ITEM        = 3
