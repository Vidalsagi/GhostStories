# first install the next:
# pip install --upgrade google-cloud-texttospeech

import os
# Imports the Google Cloud client library
from google.cloud import texttospeech
import player
from pydub import AudioSegment

path = os.getcwd()
path_up=path.split('GhostStories')[0]
credential_path = path_up+"SpeechProcess.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


class TTS():
    def __init__(self):
        self.config = ''
        self.client = texttospeech.TextToSpeechClient()  # Instantiates a client
        self.ply = player.Player()

    def tts_request(self, textstring):
        # Set the text input to be synthesized
        synthesis_input = texttospeech.SynthesisInput(text=textstring)

        # Build the voice request, select the language code ("en-US") and the ssml
        # voice gender ("neutral")
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
        )

        # Select the type of audio file you want returned
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16
        )

        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
        response = self.client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )
        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
        return response

    def save2file(self, respond):
        output = self.tts_request(respond)
        outputfilename = "C:\\Users\\Dudi\\PycharmProjects\\GhostStories\\outputGhost.wav"
        # The response's audio_content is binary.
        with open(outputfilename, 'wb') as out:
            # Write the response to the output file.
            out.write(output.audio_content)
            print('Audio content written to file: ' + outputfilename)
        # change pitch
        sound = AudioSegment.from_file('outputGhost.wav', format="wav")

        # shift the pitch up by half an octave (speed will increase proportionally)
        octaves = -0.3

        new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))

        # keep the same samples but tell the computer they ought to be played at the
        # new, higher sample rate. This file sounds like a chipmunk but has a weird sample rate.
        hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})

        # now we just convert it to a common sample rate (44.1k - standard audio CD) to
        # make sure it works in regular audio players. Other than potentially losing audio quality (if
        # you set it too low - 44.1k is plenty) this should now noticeable change how the audio sounds.
        hipitch_sound = hipitch_sound.set_frame_rate(44100)

        # Play pitch changed sound
        #play(hipitch_sound)

        # export / save pitch changed sound
        hipitch_sound.export("outputGhost1.wav", format="wav")

        self.ply.play("C:\\Users\\Dudi\\PycharmProjects\\GhostStories\\outputGhost1.wav")
