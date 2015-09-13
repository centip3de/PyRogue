import sdl2.ext

class Enemy(sdl2.ext.Entity):
    def __init__(self, world, sprite, x, y):
        self.sprite             = sprite
        self.sprite.position    = (x, y)
        self.sprite.depth       = 1
        self.enemydata          = EnemyData()

class EnemyData(object):
    def __init__(self, damage, health):
        super(EnemyData, self).__init__()
        self.damage     = damage
        self.health     = health
