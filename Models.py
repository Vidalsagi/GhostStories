from direct.gui.OnscreenText import OnscreenText
from panda3d.core import *
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence


class models():
    def __init__(self, fileName, x, y, z, xH, yH, zH, scale):
        self.fileName = fileName
        self.x = x
        self.y = y
        self.z = z
        self.xH = xH
        self.yH = yH
        self.zH = zH
        self.level = loader.loadModel(fileName)
        self.level.reparentTo(render)
        self.level.setPos(x, y, z)
        self.level.setHpr(xH, yH, zH)
        self.level.setScale(scale)

    def setHpr(self, x, y, z):
        self.level.setHpr(x, y, z)

    def setPos(self, x, y, z):
        self.level.setPos(x, y, z)


class modelList():
    def __init__(self):
        self.ghostZ = -7
        # door list
        self.doorList = doors()
        self.doorList.addDoor(models('DoorRoof1.egg', 0, 0, 0, 0, 0, 0, 1))
        self.doorList.addDoor(models('DoorRoofToStairs1.egg', 0, 0, 0, 0, 0, 0, 1))
        self.doorList.addDoor(models('DoorFloor501.egg', 0, 0, 0, 0, 0, 0, 1))
        self.doorList.addDoor(models('DoorRoof102.egg', 0, 0, 0, 0, 0, 0, 1))
        self.doorList.addDoor(models('Floor2Door02.egg', 0, 0, -3.5, 0, 0, 0, 1))
        self.doorList.addDoor(models('Floor2Door01.egg', 0, 0, -3.5, 0, 0, 0, 1))
        self.doorList.addDoor(models('ButtomFloorDoor02.egg', 0, 0, 0, 0, 0, 0, 1))
        self.doorList.addDoor(models('ButtomFloorDoor01.egg', 0, 0, 0, 0, 0, 0, 1))
        self.doorList.addDoor(models('Floor3Door01.egg', 0, 0, -3.5, 0, 0, 0, 1))
        self.level = models('cart.egg', 0, 0, -4, 0, 0, 0, 1)
        self.level = models('BookShelf1.egg', 0, 0, -4, 0, 0, 0, 1)
        self.level = models('DiningTable.egg', 0, 0, -4, 0, 0, 0, 1)
        self.level = models('GrandfatherClock.egg', 0, 0, -4, 0, 0, 0, 1)
        self.level = models('celestial.egg', 0, 0, -100, 0, 270, 0, 3)
        self.doorList.addDoor(models('WoodChair.egg', 0, 0, -3.5, 0, 0, 0, 1))
        self.doorList.addDoor(models('PictureFrame.egg', 1, 1, -4, 0, 0, 0, 1))
        self.doorList.addDoor(models('Book.egg', 1, 1, -4, 0, 0, 0, 1))
        self.level = models('knife.egg', 0, 0, -4, 0, 0, 0, 1)
        self.level = models('island.egg', 0, 0, -4, 0, 0, 0, 1)


        # castle
        self.level = models('medieval_tower_2.egg', 0, 0, 0, 0, 0, 0, 1)

        #Ghost
        self.pandaActor = Actor("Ghost.egg")
        self.pandaActor.setHpr(270, 0, 0)
        self.pandaActor.reparentTo(render)

        self.changeGoustRoom(1)

    def changeGoustRoom(self, number):
        if number == 1:
            self.ghostZ = -7
        if number == 2:
            self.ghostZ = -50

        posInterval1 = self.pandaActor.posInterval(2, Point3(0, -10, self.ghostZ), startPos=Point3(0, 30, self.ghostZ))
        hprInterval1 = self.pandaActor.hprInterval(.2, Point3(180, 0, 0), startHpr=Point3(270, 0, 0))

        posInterval2 = self.pandaActor.posInterval(2, Point3(-40, -10, self.ghostZ), startPos=Point3(0, -10, self.ghostZ))
        hprInterval2 = self.pandaActor.hprInterval(.2, Point3(90, 0, 0), startHpr=Point3(180, 0, 0))

        posInterval3 = self.pandaActor.posInterval(2, Point3(-40, 30, self.ghostZ), startPos=Point3(-40, -10, self.ghostZ))
        hprInterval3 = self.pandaActor.hprInterval(.2, Point3(0, 0, 0), startHpr=Point3(90, 0, 0))

        posInterval4 = self.pandaActor.posInterval(2, Point3(0, 30, self.ghostZ), startPos=Point3(-40, 30, self.ghostZ))
        hprInterval4 = self.pandaActor.hprInterval(.2, Point3(-90, 0, 0), startHpr=Point3(0, 0, 0))

        self.pandaPace = Sequence(posInterval1, hprInterval1, posInterval2, hprInterval2, posInterval3, hprInterval3, posInterval4, hprInterval4, name="pandaPace")
        self.pandaPace.loop()

class doors():
    def __init__(self):
        self.list = []

    def addDoor(self, objects):
        self.list.append(objects)

    def getDoor(self, name):
        for obj in self.list:
            if obj.fileName == name:
                return obj
