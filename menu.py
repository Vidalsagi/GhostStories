import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
import testPlayer

from panda3d.core import TextNode
from panda3d.core import loadPrcFileData
from direct.gui.OnscreenImage import OnscreenImage
from panda3d.core import WindowProperties
from direct.showbase.Loader import Loader
import player
import threading

# Add some text

bk_text = ""
w, h = 600, 700

props = WindowProperties()
props.setSize(w, h)

base.win.requestProperties(props)


#sound = player.Player()
#t2 = threading.Thread(target=sound.play, args=["C:\\Users\\Dudi\\PycharmProjects\\pythonProject1\\ThemeMusic.wav"])
#t2.start()

isClicked = False
imageObject = OnscreenImage(image='Menu-Image.jpg', pos=(-0.00, 0, -0.03),scale=(1.01, 1, 1.2))
textObject = OnscreenText(text=bk_text, pos=(0.70,-0.85), scale=0.07,
                          fg=(1, 0.5, 0.5, 1), align=TextNode.ACenter,
                          mayChange=1)


# Callback function to set  text
def setText():
        bk_text = ""
        textObject.setText(bk_text)
        props.setSize(1200, 800)
        props.setOrigin(-2, -2)
        base.win.requestProperties(props)
        testPlayer.FPS()
        imageObject.setScale(0, 0, 0)
        b.setPos(100, 100, 100)



# Add button
b = DirectButton(text=("Start Game"),
                 scale=.09, command=setText, pos=(-0.7, 0, -0.9))

# Run the tutorial
base.run()
