from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play
import os


def TextToSpeech(input_text):

    load_dotenv()

    elevenlabs =ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY")) 

    audio = elevenlabs.text_to_speech.convert(
        text=input_text,
        voice_id="igKQSJRWbTSeSYpQ5Zax",
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128",
    )

    play(audio)


# TextToSpeech("Hello, I am your virtual assistant. How can I help you today?")