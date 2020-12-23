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
import testPlayer


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





