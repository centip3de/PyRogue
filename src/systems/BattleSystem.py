import sdl2.ext

from components.Stats import Stats
from components.Target import Target

class BattleSystem(sdl2.ext.Applicator):
    def __init__(self):
        super(BattleSystem, self).__init__()
        self.componenttypes = Stats, Target

    def process(self, world, componentsets):
        for stats, target in componentsets:
            target.stats.health = min(0, target.stats.health - stats.strength)
            print('A target was hit for {0} damage.'.format(stats.strength))
            print("Target's new health: {0}".format(target.stats.health))
            if target.stats.health == 0:
                print('Removing target...')
                target.entity.delete()

        self.player.target = None
