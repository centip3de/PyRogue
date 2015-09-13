import sdl2.ext

from item import DataTypes
from movement import Velocity

# This gross thing handles all our collision, for now. 
class CollisionSystem(sdl2.ext.Applicator):

    def __init__(self, minx, miny, maxx, maxy):
        super(CollisionSystem, self).__init__()
        self.componenttypes = Velocity, sdl2.ext.Sprite
        self.colliders      = []
        self.collided       = []
        self.player         = None
        self.minx           = minx
        self.miny           = miny
        self.maxx           = maxx
        self.maxy           = maxy

    # Detects if any item is overlapping any other. If it is, it sets the flag in collided at the items position in colliders.
    def _overlap(self, item):
        self.collided = [None]*(len(self.colliders))
        for collider_pos, collider in enumerate(self.colliders):

            pos, sprite = item
            if sprite == collider.sprite:
                collided[collider_pos] = False
                continue

            left, top, right, bottom = sprite.area
            bleft, btop, bright, bbottom = collider.sprite.area

            self.collided[collider_pos] = (bleft < right and bright > left and btop < bottom and bbottom > top)

        return self.collided

    # Does the thing when it finds a collision. Right now that's a whole lot of nothing. 
    def process(self, world, componentsets):

        collitems = [comp for comp in componentsets if self._overlap(comp)]
        for pos, collision in enumerate(self.collided):

            if(collision):

                # Items and weapons Go straight into the inventory 
                if(self.colliders[pos].data.type == DataTypes.ITEM or self.colliders[pos].data.type == DataTypes.WEAPON):
                    thing = self.colliders[pos].data.data
                    self.colliders[pos].delete()
                    self.colliders.pop(pos)

                    print("Adding: " + thing)
                    self.player.playerdata.inventory.append(thing)
                    print("Current inventory: ", self.player.playerdata.inventory)

                # Eventually apply consumables for the player, right now they go into inventory
                elif(self.colliders[pos].data.type == DataTypes.CONSUMABLE):
                    consumable = self.colliders[pos].data.data
                    self.colliders[pos].delete()
                    self.colliders.pop(pos)

                    print("Adding: " + consumable)
                    self.player.playerdata.inventory.append(consumable)
                    print("Current inventory: ", self.player.playerdata.inventory)


                elif(self.colliders[pos].data.type == DataTypes.UNPATHABLE):
                    print("I'm on a wall!")
