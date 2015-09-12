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

    processor = sdl2.ext.TestEventProcessor()
    processor.run(window)

    sdl2.ext.quit()

if __name__ == "__main__":
    main()
