import sounddevice as sd
from scipy.io.wavfile import write
import soundfile as sf
import time

class Player():

    def __init__(self):
        self.fs = 44100  # Sample rate
        self.seconds = 3  # Duration of recording
        self.AMP = 1  # Amplify data - increase Volume of sound

    def play(self, playfilepath):
        try:
            # Extract data and sampling rate from file
            data, fs = sf.read(playfilepath, dtype='float32')
            print('Starting playing')
            sd.play(data*self.AMP, fs)
            sd.wait()  # Wait until file is done playing
            print('Stop playing')
        except:
            print('Failed in playfile operation!')