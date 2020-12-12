import tts


class Conversion():
    def __init__(self):
        self.tts = tts.TTS()

    def flaw(self, string, textObjectGhost):
        if len(string) == 0:
            self.tts.save2file("please speak again")
            return
        if 'hello' in string:
            textObjectGhost.setText('Ghost:\n What can I do for you')
            self.tts.save2file('What can I do for you')
            return
        if "what's up" in string:
            textObjectGhost.setText('Ghost:\n OK')
            self.tts.save2file('OK')
            return
        if "what is your name" in string:
            textObjectGhost.setText('Ghost:\n I forgot my name')
            self.tts.save2file("I forgot my name")
            return
        if "how can I help you" in string:
            textObjectGhost.setText('Ghost:\n you can help me by finding out my name')
            self.tts.save2file("you can help me by finding out my name")
            return
        if "what can I do" in string:
            textObjectGhost.setText('Ghost:\n this was my room, help me search for clues')
            self.tts.save2file("this was my room, help me search for clues")
            return
        else:
            textObjectGhost.setText('Ghost:\n did not get it')
            self.tts.save2file('did not get it')
            return

