import sys
import sdl2
import sdl2.ext

from player import Player

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
    factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
    sprite = factory.from_image(RESOURCES.get_path("random.bmp"))

    # Create the worl and spriterenderer system
    world = sdl2.ext.World()
    spriterenderer = SoftwareRenderer(window)
    world.add_system(spriterenderer)

    # Currently our player is the bunny picture. 
    player = Player(world, sprite, 200, 0)

    # Main event loop
    running = True
    
    while(running):

        events = sdl2.ext.get_events()

        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break

        world.process()

    return 0

if __name__ == "__main__":
    sys.exit(main())
