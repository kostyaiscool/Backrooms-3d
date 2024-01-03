from panda3d.core import Vec3
from direct.showbase.ShowBaseGlobal import globalClock
# from pausemenu import Pause
class Player:
    keyMap = {
        "forward": False,
        "backward": False,
        "left": False,
        "right": False,
    }
    SPEED = 3
    GRAVITY = -0.009
    JUMP_FORCE = 0.2
    FRICTION = -0.12
    def __init__(self, pos):
        self.model = 'sources/testmodel.obj'
        self.texture = 'sources/Image20231124120354.png'
        self.player = loader.loadModel(self.model)
        self.player.setTexture(loader.loadTexture(self.texture))
        self.player.reparentTo(render)
        self.player.setPos(pos)

        base.mouse.hideCursor(True)
        # self.pause = Pause()8

        self.position = Vec3(pos)
        self.acceleration = Vec3(0.0, 0.0, 0.0)
        self.velocity = Vec3(0.0, 0.0, 0.0)

        self.lastMouseX, self.lastMouseY = None, None
        self.rotateX, self.rotateY = 0, 0
        self.manualRecenterMouse = True
        self.is_jumping = False
        self.mouseMagnitude = 10
        self.paused = False

        self.firstFace()
        # self.collisionsCreate()
        self.events()

        # self.hideCursor(True)

        taskMgr.add(self.move, "move")
        taskMgr.add(self.mouseTask, "mouseTask")

    def updateKeyMap(self, controllName, state):
        self.keyMap[controllName] = state

    def events(self) -> None:
        base.accept("w", self.updateKeyMap, ['forward', True])
        base.accept("a", self.updateKeyMap, ['left', True])
        base.accept("s", self.updateKeyMap, ['backward', True])
        base.accept("d", self.updateKeyMap, ['right', True])
        base.accept("w-up", self.updateKeyMap, ['forward', False])
        base.accept("a-up", self.updateKeyMap, ['left', False])
        base.accept("s-up", self.updateKeyMap, ['backward', False])
        base.accept("d-up", self.updateKeyMap, ['right', False])
        base.accept('space', self.jump)
        base.accept('escape', self.superPause)

    def superPause(self):
        if self.paused == False:
            self.paused = True
            base.pause.pause()
        else:
            self.paused = False
            base.pause.unpause()


    def jump(self):
        self.is_jumping = True
        self.velocity.z = self.JUMP_FORCE

    def checkAngle(self, angle):
        if 0 <= angle < 20 or 335 <= angle < 360:
            return 0, -1
        elif 20 <= angle < 65:
            return 1, -1
        elif 65 <= angle < 110:
            return 1, 0
        elif 110 <= angle < 155:
            return 1, 1
        elif 155 <= angle < 200:
            return 0, 1
        elif 200 <= angle < 245:
            return -1, 1
        elif 245 <= angle < 290:
            return -1, 0
        elif 290 <= angle < 335:
            return -1, -1

    def move(self, task):
        dt = globalClock.getDt()

        # self.acceleration = Vec3(0, 0, self.GRAVITY)

        if self.keyMap['forward']:
            dif_x, dif_y = self.checkAngle(self.player.getH() % 360)
            self.acceleration.x = self.SPEED * dt * dif_x
            self.acceleration.y = self.SPEED * dt * dif_y
        if self.keyMap['backward']:
            # self.player.loop("walk")
            dif_x, dif_y = self.checkAngle((self.player.getH() + 180) % 360)
            self.acceleration.x = self.SPEED * dt * dif_x
            self.acceleration.y = self.SPEED * dt * dif_y
        if self.keyMap['left']:
            # self.player.loop("walk")
            dif_x, dif_y = self.checkAngle((self.player.getH() + 90) % 360)
            self.acceleration.x = self.SPEED * dt * dif_x
            self.acceleration.y = self.SPEED * dt * dif_y
        if self.keyMap['right']:
            # self.player.loop("walk")
            dif_x, dif_y = self.checkAngle((self.player.getH() + 270) % 360)
            self.acceleration.x = self.SPEED * dt * dif_x
            self.acceleration.y = self.SPEED * dt * dif_y

        self.acceleration.x += self.velocity.x * self.FRICTION
        self.acceleration.y += self.velocity.y * self.FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity + (self.acceleration * 0.5)

        # self.cTrav.traverse(render)
        # for entry in self.cHandler.getEntries():
        #     if entry.getFromNodePath().getNetTag("type") == "player":
        #         inp = entry.getFromNodePath().getPos(render)
        #         if not self.is_jumping:
        #             self.position.z = inp.z
        #         else:
        #             self.is_jumping = False
        self.player.setPos(self.position)

        return task.cont

    def mouseTask(self, task):
        mw = base.mouseWatcherNode

        hasMouse = mw.hasMouse()
        if hasMouse:
            # get the window manager's idea of the mouse position
            x, y = mw.getMouseX(), mw.getMouseY()

            if self.lastMouseX is not None:
                # get the delta
                if self.manualRecenterMouse:
                    # when recentering, the position IS the delta
                    # since the center is reported as 0, 0
                    dx, dy = x, y
                else:
                    dx, dy = x - self.lastMouseX, y - self.lastMouseY
            else:
                # no data to compare with yet
                dx, dy = 0, 0

            self.lastMouseX, self.lastMouseY = x, y

        else:
            x, y, dx, dy = 0, 0, 0, 0
        if self.manualRecenterMouse:
            # move mouse back to center
            self.recenterMouse()
            self.lastMouseX, self.lastMouseY = 0, 0

        self.rotateX += dx * 10 * self.mouseMagnitude
        self.rotateY += dy * 10 * self.mouseMagnitude

        self.player.setH(-self.rotateX)
        self.player.setP(-self.rotateY)

        return task.cont

    def recenterMouse(self):
        base.win.movePointer(
            0,
            int(base.win.getProperties().getXSize() / 2),
            int(base.win.getProperties().getYSize() / 2)
        )


    def firstFace(self):
        base.disableMouse()
        base.camera.reparentTo(self.player)
        base.camera.setH(180)
        base.camera.setPos(0, 0, 3.5)