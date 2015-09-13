import sys
import sdl2
import sdl2.ext
import random

import mapGen
from grid.GridSystem import *
from Tile import Tile
from player import Player
from movement import *
from collision import *
from item import *

# Resources file
RESOURCES = sdl2.ext.Resources(__file__, '../resources')

class SoftwareRenderer(sdl2.ext.SoftwareSpriteRenderSystem):
    def __init__(self, window):
        super(SoftwareRenderer, self).__init__(window)

    def render(self, components):
        sdl2.ext.fill(self.surface, sdl2.ext.Color(0, 0, 0))
        super(SoftwareRenderer, self).render(components)

def main():
    sdl2.ext.init()

    # Create the window
    window = sdl2.ext.Window("Foo", size=(960, 640))
    window.show()

    # Create the spirte factory and the sprite for the player
    factory         = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
    food_sprite     = factory.from_color(sdl2.ext.Color(255, 255, 255), size = (32, 32))
    weapon_sprite   = factory.from_color(sdl2.ext.Color(175, 175, 175), size = (32, 32))
    sprite          = factory.from_surface(sdl2.ext.load_image(RESOURCES.get_path('player.png')))

    # Create the worl and spriterenderer system
    world           = sdl2.ext.World()
    spriterenderer  = SoftwareRenderer(window)
    movement        = MovementSystem(0, 0, 800, 600)
    collision       = CollisionSystem(0, 0, 800, 600)

    # Add all systems to the world
    world.add_system(collision)
    world.add_system(movement)
    world.add_system(spriterenderer)

    # Test map generation
    grid = mapGen.buildMap(4)
    grid.build(world, factory)

    # Pick random location for player
    playerTile = random.choice(grid.tiles)
    player = Player(world, sprite, playerTile.sprite.position[0], playerTile.sprite.position[1])
    player_speed = 1

    gridSystem = GridSystem(960, 640, player)
    world.add_system(gridSystem)

    # Test items
    food    = Item(world, food_sprite, 500, 500, DataTypes.CONSUMABLE, "Sandwich")
    weapon  = Item(world, weapon_sprite, 300, 300, DataTypes.UNPATHABLE, "Axe")

    # Colliders for said items
    collision.colliders.append(food)
    collision.colliders.append(weapon)
    collision.player = player

    # Main event loop
    running = True
    while(running):

        events = sdl2.ext.get_events()

        for event in events:

            # Hittin' dat X button doe
            if event.type == sdl2.SDL_QUIT:
                running = False
                break

            # Movement
            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_UP:
                    player.position.y -= 1

                elif event.key.keysym.sym == sdl2.SDLK_DOWN:
                    player.position.y += 1

                elif event.key.keysym.sym == sdl2.SDLK_LEFT:
                    player.position.x -= 1

                elif event.key.keysym.sym == sdl2.SDLK_RIGHT:
                    player.position.x += 1

        sdl2.SDL_Delay(10)
        world.process()

    return 0

if __name__ == "__main__":
    sys.exit(main())
