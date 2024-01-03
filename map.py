class Map:
    def __init__(self, pos):
        self.model = 'sources/lvl0.obj'
        self.texture = 'sources/untitled.png'
        self.player = loader.loadModel(self.model)
        self.player.setTexture(loader.loadTexture(self.texture))
        self.player.reparentTo(render)
        self.player.setPos(pos)

