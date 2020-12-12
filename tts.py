# first install the next:
# pip install --upgrade google-cloud-texttospeech

import os
# Imports the Google Cloud client library
from google.cloud import texttospeech
import player

credential_path = "C:\\Users\\Sagi\\Desktop\\Code\\SpeechProcess-dbe0d5614ee0.json"
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
        outputfilename = "C:\\Users\\Sagi\\PycharmProjects\\GhostStories\\outputGhost.wav"
        # The response's audio_content is binary.
        with open(outputfilename, 'wb') as out:
            # Write the response to the output file.
            out.write(output.audio_content)
            print('Audio content written to file: ' + outputfilename)
        self.ply.play("C:\\Users\\Sagi\\PycharmProjects\\GhostStories\\outputGhost.wav")
