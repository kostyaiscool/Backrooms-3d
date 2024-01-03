from direct.showbase.ShowBase import ShowBase
from mouseset import mouse
from player import Player
from map import Map
from pausemenu import Menu, Pause
class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.menu = Menu()
        self.pause = Pause()
    def startGame(self):
        # self.mouse = mouse
        self.menu.panel.hide()
        self.player = Player((0, 10, 0))
        self.map = Map((0, 0, 0))
    def stopGame(self):
        # self.mouse = mouse
        self.pause.panel.hide()
        self.menu.panel.show()

game = Game()
game.run()
