"""
awsd - movement
mouse - look around
p - talk
r - get back to start
"""

import direct.directbase.DirectStart
import panda3d

from direct.showbase.ShowBaseGlobal import globalClock
from pandac.PandaModules import *
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import *
import sys
import panda3d
import speech
import threading
import tests
import Models
from direct.gui.OnscreenImage import OnscreenImage
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence


class FPS(object):
    """
        This is a very simple FPS like -
         a building block of any game i guess
    """

    def __init__(self):
        """ create a FPS type game """
        self.initCollision()
        self.loadLevel()
        self.initPlayer()
        base.accept("escape", sys.exit)
        base.disableMouse()
        OnscreenText(text=__doc__, style=1, fg=(1, 1, 1, 1),
                     pos=(-1.3, 0.95), align=TextNode.ALeft, scale=.05)

    def initCollision(self):
        """ create the collision system """
        base.cTrav = CollisionTraverser()
        base.pusher = CollisionHandlerPusher()

    def loadLevel(self):
        #shelfs
        self.level = loader.loadModel('Shelfs.egg')
        self.level.reparentTo(render)
        self.level.setPos(0, 0, 0)
        self.level.setScale(1)  # Uniform scaling of the model

        # Castle
        self.modelArr = Models.modelList()

        # Desert
        self.level = loader.loadModel('medieval_tower_2.egg')
        self.level.reparentTo(render)
        self.level.setPos(0, 0, 0)
        self.level.setScale(1)  # Uniform scaling of the model

        #chair
        self.model = loader.loadModel("WoodChair.egg")
        self.model.setScale(1)  # Uniform scaling of the model
        self.model.setPos(0, 13, -10)  # Location (x, y, z)
        self.model.setHpr(180, 0, 0)  # Orientation in degrees (Heading, Pitch, Roll)
        # Adding the model to the Scene Graph under the root
        self.model.setCollideMask(0)
        self.model.reparentTo(render)


        #sky
        self.model = loader.loadModel("celestial.egg")
        self.model.setScale(2.4)
        self.model.setPos(0, 0, 210)
        self.model.setHpr(0, 270, 0)
        self.model.reparentTo(render)


    def initPlayer(self):
        """ loads the player and creates all the controls for him"""
        self.node = Player(self.modelArr)

# object
class Player(object):
    """
        Player is the main actor in the fps game
    """
    speed = 10
    FORWARD = Vec3(0, 2, 0)
    BACK = Vec3(0, -1, 0)
    LEFT = Vec3(-1, 0, 0)
    RIGHT = Vec3(1, 0, 0)
    STOP = Vec3(0)
    walk = STOP
    strafe = STOP
    readyToJump = False
    jump = 0
    talk = False
    reSpawn = False
    sp = speech.Speech()
    isTrue = tests.Bool()
    beginingConv = "suggestions:\n1)Who are you and what is this place?\n2)hello\n3)how can i help you?"

    textObject = OnscreenText(text='my text string', pos=(-1.3, -0.8), scale=0.1, bg=(10, 10, 10, 10))
    textObject.setText("Welcome to GhostStories ")
    textObject.setAlign(TextNode.ALeft)

    textObjectGhost = OnscreenText(text='my text string', pos=(1.2, 0.6), scale=0.1, bg=(10, 10, 10, 10))
    textObjectGhost.setText("")
    textObjectGhost.setAlign(TextNode.ARight)

    textObjectConv = OnscreenText(text='my text string', pos=(0.3, -0.5), scale=0.1, bg=(10, 10, 10, 10))
    textObjectConv.setText(beginingConv)
    textObjectConv.setScale(0.06)
    textObjectConv.setAlign(TextNode.ALeft)


    def __init__(self, modelArr):
        """ inits the player """
        self.modelArr = modelArr
        self.loadModel()
        self.setUpCamera()
        self.createCollisions()
        self.attachControls()
        # init mouse update
        taskMgr.add(self.mouseUpdate, 'mouse-task')
        taskMgr.add(self.moveUpdate, 'move-task')
        taskMgr.add(self.jumpUpdate, 'jump-task')
        taskMgr.add(self.talkUpdate, 'talk-task')



    def loadModel(self):
        """ make the nodepath for player """
        self.node = NodePath('player')
        self.node.reparentTo(render)
        self.node.setPos(0, 0, 150 )
        self.node.setScale(1)

    def setUpCamera(self):
        """ puts camera at the players node """
        pl = base.cam.node().getLens()
        pl.setFov(70)
        base.cam.node().setLens(pl)
        base.camera.reparentTo(self.node)

    def createCollisions(self):
        """ create a collision solid and ray for the player """
        cn = CollisionNode('player')
        cn.addSolid(CollisionSphere(0, 0, 0, 5))
        solid = self.node.attachNewNode(cn)
        base.cTrav.addCollider(solid, base.pusher)
        base.pusher.addCollider(solid, self.node, base.drive.node())
        # init players floor collisions
        ray = CollisionRay()
        ray.setOrigin(0, 0, -.2)
        ray.setDirection(0, 0, -1)
        cn = CollisionNode('playerRay')
        cn.addSolid(ray)
        cn.setFromCollideMask(BitMask32.bit(0))
        cn.setIntoCollideMask(BitMask32.allOff())
        solid = self.node.attachNewNode(cn)
        self.nodeGroundHandler = CollisionHandlerQueue()
        base.cTrav.addCollider(solid, self.nodeGroundHandler)

    def attachControls(self):
        """ attach key events """
        base.accept("space", self.__setattr__, ["readyToJump", True])
        base.accept("space-up", self.__setattr__, ["readyToJump", False])
        base.accept("s", self.__setattr__, ["walk", self.STOP])
        base.accept("w", self.__setattr__, ["walk", self.FORWARD])
        base.accept("s", self.__setattr__, ["walk", self.BACK])
        base.accept("s-up", self.__setattr__, ["walk", self.STOP])
        base.accept("w-up", self.__setattr__, ["walk", self.STOP])
        base.accept("a", self.__setattr__, ["strafe", self.LEFT])
        base.accept("d", self.__setattr__, ["strafe", self.RIGHT])
        base.accept("a-up", self.__setattr__, ["strafe", self.STOP])
        base.accept("d-up", self.__setattr__, ["strafe", self.STOP])
        base.accept("p", self.__setattr__, ["talk", True])
        base.accept("p-up", self.__setattr__, ["talk", False])
        base.accept("r", self.__setattr__, ["reSpawn", True])
        base.accept("r-up", self.__setattr__, ["reSpawn", False])

    def mouseUpdate(self, task):
        """ this task updates the mouse """
        md = base.win.getPointer(0)
        x = md.getX()
        y = md.getY()
        if base.win.movePointer(0, 600, 400):
            self.node.setH(self.node.getH() - (x - 600) * 0.1)
            base.camera.setP(base.camera.getP() - (y - 400) * 0.1)
        return task.cont
        #base.win.getXSize()
    def moveUpdate(self, task):
        """ this task makes the player move """
        # move where the keys set it
        self.node.setPos(self.node, self.walk * globalClock.getDt() * self.speed)
        self.node.setPos(self.node, self.strafe * globalClock.getDt() * self.speed)
        return task.cont

    def jumpUpdate(self, task):
        """ this task simulates gravity and makes the player jump """
        # get the highest Z from the down casting ray
        highestZ = -100

        # gravity effects and jumps
        self.node.setZ(self.node.getZ() + self.jump * globalClock.getDt())
        self.jump -= 1 * globalClock.getDt()
        if highestZ > self.node.getZ() - .3:
            self.jump = 0
            self.node.setZ(highestZ + .3)
            if self.readyToJump:
                self.jump = 1
        return task.cont

    def talkUpdate(self, task):
        if self.talk:
            if self.isTrue.isTrue:
                self.isTrue.change()
                t1 = threading.Thread(target=self.sp.record, args=[self.textObject, self.isTrue, self.textObjectGhost, self.textObjectConv, self.modelArr])
                t1.start()

        if self.reSpawn:
            self.node.setPos(20, 0, 200)
        return task.cont
