import sdl2.ext
import random
from components.Stats import Stats
from components.Position import Position
from entities.Item import DataTypes

RESOURCES = sdl2.ext.Resources(__file__, "../../resources")

class Enemy(sdl2.ext.Entity):
    def __init__(self, world, factory, x, y):
        self.sprite             = factory.from_image(RESOURCES.get_path('enemy.png'))
        self.position           = Position(x, y)
        self.sprite.depth       = 2
        self.stats              = Stats(20, 20)
        self.enemydata          = EnemyData(20, 20)

    def random_move(self, grid):
        while True:
            num = random.random()

            if num > 0.75:
                x = self.position.x
                y = self.position.y + 1
            elif num > 0.50:
                x = self.position.x + 1
                y = self.position.y
            elif num > 0.25:
                x = self.position.x - 1
                y = self.position.y
            else:
                x = self.position.x
                y = self.position.y - 1

            if grid.hasTileAt(x, y):
                self.position = Position(x, y)
                break

class EnemyData(object):
    def __init__(self, damage, health):
        super(EnemyData, self).__init__()
        self.damage     = damage
        self.health     = health
        self.type       = DataTypes.ENTITY
        self.data       = "Enemy"
