import sounddevice
import scipy
from scipy.io.wavfile import write
import io
import os
from google.cloud import speech
from direct.gui.OnscreenText import OnscreenText
import panda3d
import threading
import tests


class Speech():
    def __init__(self):
        self.fs = 44100
        self.second = 2

    def record(self, textObject, isTalk):
        record_voice = sounddevice.rec(int(self.second * self.fs), samplerate=self.fs, channels=1, dtype='int16')
        sounddevice.wait()
        write("output.wav", self.fs, record_voice)

        credential_path = "C:\\Users\\Sagi\\Desktop\\Code\\SpeechProcess-dbe0d5614ee0.json"
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

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
            string = format(result.alternatives[0].transcript) + "\nConfidence:" + format(result.alternatives[0].confidence)
            if string:
                textObject.setText(string)
            else:
                textObject.setText('Please Speak Again')

        isTalk.change()
        return
