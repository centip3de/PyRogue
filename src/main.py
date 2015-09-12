import sys
import sdl2
import sdl2.ext

RESOURCES = sdl2.ext.Resources(__file__, '../resources')

def main():
    sdl2.ext.init() 

    window = sdl2.ext.Window("Foo", size=(800, 600))
    window.show()

    factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
    sprite = factory.from_image(RESOURCES.get_path("random.bmp"))

    spriterenderer = factory.create_sprite_render_system(window)
    spriterenderer.render(sprite)

    running = True
    while(running):
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
        window.refresh()

    return 0

if __name__ == "__main__":
    sys.exit(main())
