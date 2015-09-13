class Grid:
    def __init__(self):
        self.rooms = []
        self.corridors = []
        self.tiles = []

    def build(self, world, factory):
        self.tiles = []

        for room in self.rooms:
            self.tiles += room.build(world, factory)

        for corridor in self.corridors:
            self.tiles += corridor.build(world, factory)

    def connected(self, room1, room2):
        for corridor in self.corridors:
            if corridor.room1.pos == room1.pos and corridor.room2.pos == room2.pos:
                return True
            elif corridor.room1.pos == room2.pos and corridor.room2.pos == room1.pos:
                return True
        return False

    def entitiesAt(self, x, y):
        entities = []

        for room in self.rooms:
            for item in room.items:
                if item.position.x == x and item.position.y == y:
                    entities.append(item)

        for tile in self.tiles:
            if tile.position.x == x and tile.position.y == y:
                entities.append(tile)

        return entities
