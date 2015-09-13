import sdl2.ext

from components.Velocity import Velocity
from entities.PlayerData import PlayerData
from entities.PlayerData import Equippable
from components.Position import Position
from entities.Item       import WeaponTypes
from entities.Item       import ConsumableTypes

class Player(sdl2.ext.Entity):
    def __init__(self, world, sprite, x, y):
        self.sprite             = sprite
        self.position           = Position(x, y)
        self.sprite.depth       = 2
        self.playerdata         = PlayerData()

    def walk(self, grid, direction):
        x = self.position.x + direction.value.x
        y = self.position.y + direction.value.y

        if grid.hasTileAt(x, y):
            self.position = Position(x, y)

    def take_damage(self, amount):
        self.playerdata.health -= amount
        if(self.playerdata.health <= 0):
            return "Ded"

    def get_damage(self):
        if(self.playerdata.equipped[Equippable.WEAPON] == None):
            return 1

        elif(self.playerdata.equipped[Equippable.WEAPON] == WeaponTypes.STICK):
            return 5

        elif(self.playerdata.equipped[Equippable.WEAPON] == WeaponTypes.AXE):
            return 10

    def consume(self):
        if(self.playerdata.equipped[Equippable.CONSUMABLE] == None):
            self.playerdata.health += 0

        elif(self.playerdata.equipped[Equippable.CONSUMABLE] == ConsumableTypes.SANDWICH):
            self.playerdata.health += 10

        self.playerdata.equipped[Equippable.CONSUMABLE] == None
