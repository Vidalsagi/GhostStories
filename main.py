import sys
from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from direct.showbase.ShowBaseGlobal import globalClock
from direct.task import Task
from direct.interval.IntervalGlobal import Sequence
#from panda3d.core import Point3
from panda3d.core import *
from direct.gui.OnscreenText import OnscreenText
import panda3d
import speech
import threading
import tests

keymap = {
    "up": False,
    "down": False,
    "left": False,
    "right": False,
    "p": False
}


def updateKey(key, state):
    keymap[key] = state


class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.x = 0
        self.y = 0
        self.sp = speech.Speech()
        self.isTrue = tests.Bool()

        self.disableMouse()

        self.wp = panda3d.core.WindowProperties()
        self.wp.setSize(1200, 800)
        self.win.requestProperties(self.wp)
        self.camera.setPos(0, 0, 8)

        # Load the bedroom environment model.
        self.scene = self.loader.loadModel("models/bedroom")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(5, 5, 5)
        self.scene.setPos(0, 0, -20)

        # Load the television  model.
        self.model = self.loader.loadModel("television.egg")
        self.model.setScale(10)  # Uniform scaling of the model
        self.model.setPos(-40, 60, -8)  # Location (x, y, z)
        self.model.setHpr(45, 0, 0)  # Orientation in degrees (Heading, Pitch, Roll)
        # Adding the model to the Scene Graph under the root
        self.model.reparentTo(self.render)

        # Load the Ghost  model.
        self.model = self.loader.loadModel("Ghost.egg")
        self.model.setScale(0.08)  # Uniform scaling of the model
        self.model.setPos(40, 60, -6)  # Location (x, y, z)
        self.model.setHpr(135, 0, 0)  # Orientation in degrees (Heading, Pitch, Roll)
        # Adding the model to the Scene Graph under the root
        self.model.reparentTo(self.render)

        self.accept("arrow_left", updateKey, ["left", True])
        self.accept("arrow_left-up", updateKey, ["left", False])
        self.accept("arrow_right", updateKey, ["right", True])
        self.accept("arrow_right-up", updateKey, ["right", False])
        self.accept("p", updateKey, ["p", True])

        self.accept("arrow_up", updateKey, ["up", True])
        self.accept("arrow_up-up", updateKey, ["up", False])
        self.accept("arrow_down", updateKey, ["down", True])
        self.accept("arrow_down-up", updateKey, ["down", False])
        self.accept("p-up", updateKey, ["p", False])

        self.task_mgr.add(self.update, "update")

        self.textObject1 = OnscreenText(text='Player', pos=(-1.3, -0.6), scale=0.1, bg=(10, 10, 10, 10))
        self.textObject = OnscreenText(text='my text string', pos=(-1.4, -0.75), scale=0.1, bg=(10, 10, 10, 10))
        self.textObject.setText("Speak with the ghost")
        self.textObject.setAlign(TextNode.ALeft)
        self.set_background_color(10, 10, 10, 10)

    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

    def update(self, task):
        dt = globalClock.getDt()

        if keymap["left"]:
            self.x += 1
        if keymap["right"]:
            self.x -= 1
        if keymap["up"]:
            self.camera.setY(self.camera, 1.5)
        if keymap["down"]:
            self.camera.setY(self.camera, -0.3)
        if keymap["p"]:
            self.textObject1.setText("You:")
            self.textObject.setText("please talk...")
            if self.isTrue.isTrue:
                self.isTrue.change()
                t1 = threading.Thread(target=self.sp.record, args=[self.textObject, self.isTrue])
                t1.start()

        self.camerapos(self.x, self.y)
        return task.cont

    def camerapos(self, x, y):
        self.camera.setHpr(x, 0, 0)
        # self.camera.setPos(0, y, 5)



app = MyApp()
app.run()

'''
 string = self.sp.record()
            if string:
                self.textObject.setText(string)
'''
