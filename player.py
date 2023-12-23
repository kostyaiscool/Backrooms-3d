class Player:
    def __init__(self):
        self.model = 'sources/testmodel.blend'
        self.player = loader.loadModel(self.model)
        self.player.reparent(render)
        self.player.setPos(0, 10, 0)

player = Player()