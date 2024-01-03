from direct.task.Task import Task
from direct.task.TaskManagerGlobal import taskMgr
from panda3d.core import WindowProperties


class Mouse:
    def __init__(self):
        # base.disableMouse()

        # control mapping of mouse movement to box movement
        self.mouseMagnitude = 1

        self.rotateX, self.rotateY = 0, 0
        self.hideMouse = False
        self.manualRecenterMouse = False
        self.lastMouseX, self.lastMouseY = None, None
        taskMgr.add(self.mouseTask, "Mouse Task")
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

        # scale position and delta to pixels for user
        w, h = base.win.getSize()



        # rotate box by delta
        self.rotateX += dx * 10 * self.mouseMagnitude
        self.rotateY += dy * 10 * self.mouseMagnitude


        # self.model.setH(self.rotateX)
        # self.model.setP(self.rotateY)
        return Task.cont

    def recenterMouse(self):
        base.win.movePointer(0,
              int(base.win.getProperties().getXSize() / 2),
              int(base.win.getProperties().getYSize() / 2))
        
    def hideCursor(self, mouseFlag):
        """Hide the mouse"""
        wp = WindowProperties()
        wp.setCursorHidden(mouseFlag)
        base.win.requestProperties(wp)

