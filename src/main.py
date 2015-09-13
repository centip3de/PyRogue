import sys
import sdl2
import sdl2.ext

import mapGen
from Tile import Tile
from player import Player
from movement import *
from collision import *

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
    window = sdl2.ext.Window("Foo", size=(800, 600))
    window.show()

    # Create the spirte factory and the sprite for the player
    factory         = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
    sprite          = factory.from_image(RESOURCES.get_path("random.bmp"))

    # Create the worl and spriterenderer system
    world           = sdl2.ext.World()
    spriterenderer  = SoftwareRenderer(window)
    movement        = MovementSystem(0, 0, 800, 600)
    collision       = CollisionSystem(0, 0, 800, 600)

    # Add all systems to the world
    world.add_system(collision)
    world.add_system(movement)
    world.add_system(spriterenderer)

    # Currently our player is the bunny picture.
    player = Player(world, sprite, 200, 200)
    player_speed = 2

    mapData = mapGen.buildMap(5, 5)
    for room in mapData:
        room.buildTiles(world, factory)

    # Main event loop
    running = True

    while(running):

        events = sdl2.ext.get_events()

        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break

            if event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == sdl2.SDLK_UP:
                    player.velocity.vy = -player_speed

                elif event.key.keysym.sym == sdl2.SDLK_DOWN:
                    player.velocity.vy = player_speed

                elif event.key.keysym.sym == sdl2.SDLK_LEFT:
                    player.velocity.vx = -player_speed

                elif event.key.keysym.sym == sdl2.SDLK_RIGHT:
                    player.velocity.vx = player_speed

            elif event.type == sdl2.SDL_KEYUP:
                player.velocity.vy = 0
                player.velocity.vx = 0

        sdl2.SDL_Delay(10)
        world.process()

    return 0

if __name__ == "__main__":
    sys.exit(main())
