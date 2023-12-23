from direct.showbase.ShowBase import ShowBase
from mouseset import mouse
from player import player

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.mouse = mouse
        self.player = player


game = Game()
game.run()
