
from direct.showbase.ShowBase import ShowBase
#from panda3d.core import Point3
import speech
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
        self.loadSound()
        self.x = 0
        self.y = 0
        self.sp = speech.Speech()
        self.isTrue = tests.Bool()
        #self.initCollision()
        #self.loadLevel()
        #self.initPlayer(s)
        self.disableMouse()





