import sdl2.ext
from components.Position import Position
from entities.Item import DataTypes

RESOURCES = sdl2.ext.Resources(__file__, "../../resources")

class Enemy(sdl2.ext.Entity):
    def __init__(self, world, factory, x, y):
        self.sprite             = factory.from_image(RESOURCES.get_path('enemy.png')) 
        self.position           = Position(x, y)
        self.sprite.depth       = 2
        self.enemydata          = EnemyData(20, 20)

class EnemyData(object):
    def __init__(self, damage, health):
        super(EnemyData, self).__init__()
        self.damage     = damage
        self.health     = health
        self.type       = DataTypes.ENTITY
        self.data       = "Enemy"
