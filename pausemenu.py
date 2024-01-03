from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectButton import DirectButton
from sys import exit
class Menu:
    def __init__(self):
        self.panel = DirectFrame(frameColor = (0, 0, 0, 0.5), frameSize = (-1, 1, -1, 1))
        self.button1 = DirectButton(text='Start game', scale=0.2, parent=self.panel, command=base.startGame)
        self.button2 = DirectButton(text='Quit', scale=0.2, parent=self.panel, command=exit)
        self.button1.setPos(0, 0, 0.2)
        self.button2.setPos(0, 0, -0.2)
class Pause:
    def __init__(self):
        self.panel = DirectFrame(frameColor=(0, 0, 0, 0.5), frameSize=(-1, 1, -1, 1))
        self.button1 = DirectButton(text='Continue', scale=0.2, parent=self.panel, command=self.unpause)
        self.button2 = DirectButton(text='Main menu', scale=0.2, parent=self.panel, command=base.stopGame)
        self.button1.setPos(0, 0, 0.2)
        self.button2.setPos(0, 0, -0.2)
        self.panel.hide()
    def unpause(self):
        self.panel.hide()
        taskMgr.add(self.move, "move")
        taskMgr.add(self.mouseTask, "mouseTask")
    def pause(self):
        self.panel.show()
        taskMgr.remove("move")
        taskMgr.remove("mouseTask")
        base.mouse.hideCursor(False)