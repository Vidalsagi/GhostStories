import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from panda3d.core import *
from direct.gui.DirectGui import DirectFrame

myFrame = DirectFrame(frameColor=(0, 0, 0, 1),
                      frameSize=(-1, 1, -1, 1),
                      pos=(1, -1, -1))
# Add some text
bk_text = "GhostStories"
textObject = OnscreenText(text=bk_text, pos=(0, 0.5), scale=0.3,
                          fg=(0, 0.5, 0.5, 1), align=TextNode.ACenter,
                          mayChange=1)

# Add some text
output = "Select your option"
textObject = OnscreenText(text=output, pos=(0, 0.2), scale=0.07,
                          fg=(0, 0.5, 0.5, 1), align=TextNode.ACenter,
                          mayChange=1)

# Callback function to set  text
def itemSel(arg):
    output = "Item Selected is: " + arg
    textObject.setText(output)

# Callback function to set  text
def setText():
        bk_text = "Button Clicked"
        textObject.setText(bk_text)

# Add button
b = DirectButton(text=("Start Game", "click!", "rolling over", "disabled"),
                 scale=0.3, command=setText)

d = DirectButton(text=("Start Game", "click!", "rolling over", "disabled"),
                scale=0.5, command=setText)

# Create a frame
menu = DirectOptionMenu(text="options", scale=0.2, command=itemSel,
                        items=["item1", "item2", "item3"], initialitem=2,
                        highlightColor=(0.2, 0.2, 0.2, 1))


# Run the tutorial
base.run()