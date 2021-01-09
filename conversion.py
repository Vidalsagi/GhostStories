import tts


class Conversion():
    def __init__(self):
        self.tts = tts.TTS()
        self.branch = 0

    def flaw(self, string, textObjectGhost, textObjectConv, modelArr):
        # branch 0 start of the game*************************************************************************************
        if self.branch == 0:
            if "what is this place" == string:
                textObjectGhost.setText('Ghost:\n This was my home,\n can you tell me how did you get here?')
                self.branch = 0.1
                self.suggestionsChange(textObjectConv, self.branch, modelArr)
                self.tts.save2file('This was my home, can you tell me how did you get here?')
                return

        if self.branch == 0.1:
            if "I'm not sure" == string or "I am not sure" == string:
                textObjectGhost.setText('Ghost:\nThis room downstairs is full with clues about my name,\n help me search for these clues so that I ll remember')
                self.branch = 0.2
                self.suggestionsChange(textObjectConv, self.branch, modelArr)
                self.tts.save2file('This room downstairs is full with clues about my name, help me search for these clues so that I ll remember')
                return
            if 'What are you talking about' == string or "I'm tired I want to sleep a bit" == string or "I'm tired I went to sleep a bit" == string:
                textObjectGhost.setText('Ghost:\n Rude')
                self.tts.save2file('Rude')
                return

        if self.branch == 0.2:
            if "what should I do next" == string:
                textObjectGhost.setText('Ghost:\nThe door behind you opened,go downstairs and look around')
                self.branch = 1
                self.suggestionsChange(textObjectConv, self.branch, modelArr)
                self.tts.save2file('The door behind you opened,go downstairs and look around')
                return
            if 'i want to go home' == string:
                textObjectGhost.setText('Ghost:\nYou will never go home')
                self.tts.save2file('You will never go home')
                return
            if 'let me out' == string:
                textObjectGhost.setText("Ghost:\nDon't push me!")
                self.tts.save2file("Don't push me!")
                return

        # branch 1 first room*********************************************************************************************
        if self.branch == 1:
            if "s" == string or "S" == string:
                textObjectGhost.setText('Ghost:\nThis is correct!\nmy name start with S,\nlook for my second letter')
                self.branch = 1.1
                self.suggestionsChange(textObjectConv, self.branch, modelArr)
                self.tts.save2file('This is correct! my name start with S, look for my second letter')
                return
            else:
                textObjectGhost.setText('Ghost:\nThis is not my first letter!')
                self.tts.save2file('This is not my first letter')
                return

        if self.branch == 1.1:
            if "h" == string or "H" == string:
                textObjectGhost.setText('Ghost:\nThis is correct!\nlook for my third letter')
                self.branch = 1.2
                self.suggestionsChange(textObjectConv, self.branch, modelArr)
                self.tts.save2file('This is correct!look for my third letter')
                return
            else:
                textObjectGhost.setText('Ghost:\nThis is not my second letter!')
                self.tts.save2file('This is not my second letter')
                return

        if self.branch == 1.2:
            if "a" == string or "A" == string:
                textObjectGhost.setText('Ghost:\nThis is correct!\nmy name is sha..\nlook for my fourth letter')
                self.branch = 1.3
                self.suggestionsChange(textObjectConv, self.branch, modelArr)
                self.tts.save2file('This is correct!my name is sha.., look for my fourth letter')
                return
            else:
                textObjectGhost.setText('Ghost:\nThis is not my third letter!')
                self.tts.save2file('This is not my third letter')
                return

        if self.branch == 1.3:
            if "y" == string or "Y" == string or "why" == string:
                textObjectGhost.setText('Ghost:\nThis is correct!\nmy name is Shay\ngo now to the next room')
                self.branch = 1.4
                self.suggestionsChange(textObjectConv, self.branch, modelArr)
                self.tts.save2file('This is correct!my name is Shay , go now to the next room')
                return
            else:
                textObjectGhost.setText('Ghost:\nThis is not my fourth letter!')
                self.tts.save2file('This is not my fourth letter')
                return

        if self.branch == 1.4:
            if "please let me go" == string:
                textObjectGhost.setText('Ghost:\nBut we just started to know each other better,\nlets continue')
                self.tts.save2file('But we just started to know each other better, lets continue')
                return
            if 'what now' == string:
                self.branch = 2
                self.suggestionsChange(textObjectConv, self.branch, modelArr)
                textObjectGhost.setText('Ghost:\nGo downstairs,and find the next clue')
                self.tts.save2file('Go downstairs,and find the next clue')
                return
            if 'you have a stupid name' == string:
                textObjectGhost.setText("Ghost:\nAnd you have a stupid face")
                self.tts.save2file("And you have a stupid face!")
                return

        # branch 2 second room******************************************************************************

        # default*******************************************************************************************
        if len(string) == 0:
            self.tts.save2file("please speak again")
            return

        if 'hello' in string:
            textObjectGhost.setText('Ghost:\nWhat can I do for you')
            self.tts.save2file('What can I do for you')
            return
        if "what's up" in string:
            textObjectGhost.setText('Ghost:\n OK')
            self.tts.save2file('OK')
            return
        if "what is your name" in string:
            textObjectGhost.setText('Ghost:\nI forgot my name')
            self.tts.save2file("I forgot my name")
            return
        if "how can I help you" in string:
            textObjectGhost.setText('Ghost:\nYou can help me by finding out my name')
            self.tts.save2file("you can help me by finding out my name")
            return
        if "what can I do" in string:
            textObjectGhost.setText('Ghost:\nThis was my room, help me search for clues')
            self.tts.save2file("this was my room, help me search for clues")
            return
        else:
            textObjectGhost.setText('Ghost:\nDid not get it')
            self.tts.save2file('Did not get it')
            return

    def suggestionsChange(self, textObjectConv, place, modelArr):
        if place == 0:
            textObjectConv.setText("suggestions:\n1)what is this place?\n2)Hello\n3)How can I help you?")
        if place == 0.1:
            textObjectConv.setText("suggestions:\n1)I'm not sure\n2)What are you talking about?\nthis is my room\n3)I'm tired, I want to sleep a bit")
        if place == 0.2:
            textObjectConv.setText("suggestions:\nFind the first letter!\n1)I want to go home\n2)Let me out\n3)What should I do next?")
            modelArr.doorList.getDoor('DoorRoofToStairs1.egg').setHpr(90, 0, 0)
            modelArr.doorList.getDoor('DoorRoofToStairs1.egg').setPos(67, 15, 0)
            modelArr.doorList.getDoor('DoorRoofToStairs1.egg').level.setCollideMask(0)
            modelArr.changeGoustRoom(2)
        if place == 1:
            textObjectConv.setText("suggestions:\nFind the first letter:\nThe first letter is _")
        if place == 1.1:
            textObjectConv.setText("suggestions:\nFind the second letter:\nThe second letter is _")
        if place == 1.2:
            textObjectConv.setText("suggestions:\nFind the third letter:\nThe third letter is _")
        if place == 1.3:
            textObjectConv.setText("suggestions:\nFind the fourth letter:\nThe fourth letter is _")
        if place == 1.4:
            textObjectConv.setText("suggestions:\n1)please let me go\n2)what now\n3)you have a stupid name")
        if place == 2:
            textObjectConv.setText("suggestions:\n***room 2 TBC***")
            modelArr.doorList.getDoor('DoorFloor105.egg').level.hide()
            modelArr.doorList.getDoor('DoorFloor105.egg').level.setCollideMask(0)




