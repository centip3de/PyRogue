class Grid:
    def __init__(self):
        self.rooms = []
        self.corridors = []

    def build(self, world, factory):
        self.tiles = []

        for room in self.rooms:
            self.tiles += room.build(world, factory)

        for corridor in self.corridors:
            self.tiles += corridor.build(world, factory)
