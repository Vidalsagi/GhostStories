import sounddevice
from scipy.io.wavfile import write
import io
import os
from google.cloud import speech
import conversion
import tts

path = os.getcwd()
path_up=path.split('GhostStories')[0]
credential_path = path_up+"SpeechProcess.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


class Speech():
    def __init__(self):
        self.fs = 44100
        self.second = 3
        self.tts = tts.TTS()
        self.conv = conversion.Conversion()


    def record(self, textObject, isTalk , textObjectGhost,textObjectConv, modelArr):
        record_voice = sounddevice.rec(int(self.second * self.fs), samplerate=self.fs, channels=1, dtype='int16')
        sounddevice.wait()
        write("output.wav", self.fs, record_voice)
        client = speech.SpeechClient()
        file_name = os.path.join(
            os.path.dirname(__file__),
            'output.wav')

        with io.open(file_name, 'rb') as audio_file:
            content = audio_file.read()
            audio = speech.RecognitionAudio(content=content)

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code="en-US")

        response = client.recognize(config=config, audio=audio)
        for result in response.results:
            string = format(result.alternatives[0].transcript)
            textObject.setText("Player: \n" + string)
            self.conv.flaw(string, textObjectGhost, textObjectConv, modelArr)
        isTalk.change()
        return
