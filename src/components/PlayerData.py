class PlayerData(object):
    def __init__(self):
        super(PlayerData, self).__init__()
        self.inventory  = []
        self.health     = 50
        self.equipped   = {}
