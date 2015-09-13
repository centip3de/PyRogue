import sdl2.ext

from components.Target import Target
from components.Position import Position
from entities.Tile import Tile
from entities.Enemy import Enemy
from entities.Item import Item

class PlayerMovementSystem(sdl2.ext.Applicator):
    def __init__(self):
        self.componenttypes = []

    def walk(self, direction):
        x = self.player.position.x + direction.value.x
        y = self.player.position.y + direction.value.y

        entities = self.grid.entitiesAt(x, y)
        if not any([type(entity) is Tile for entity in entities]):
            return

        move = True

        for entity in entities:
            ty = type(entity)

            if ty is Enemy:
                print('Setting player target')
                self.player.target = Target(entity.stats, entity)
                move = False

        if move:
            self.player.position = Position(x, y)

    def process(self, world, componentsets):
        pass
