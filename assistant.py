import speech2Text
from ollama import chat

from gtts import gTTS
import os

import pyttsx3

from elevenlabs.client import ElevenLabs
from elevenlabs import ElevenLabs, VoiceSettings

import uuid

from config import ELEVEN_LABS_API_KEY

client = ElevenLabs(
  api_key= ELEVEN_LABS_API_KEY,
)
print("🐍 File: ai-asistant/assistant.py | Line: 15 | undefined ~ client",client)

def chatfun():
    while True:
        request = speech2Text.record_voice()
        response = chat(
            model = 'gemma2',
            messages = [{'role': 'user', 'content': request}],
            stream = True,
        )
        
        spoken_text = ''

        for chunk in response:
            ctext = chunk['message']['content']
            spoken_text += ctext
        print("spoken_text is generated..")
        print(f"{spoken_text}")

        filtered_text = filter_text(spoken_text)
        saved_audio_path = text2Speech_elevenlabs(filtered_text, 'en-US')
        play_audio(saved_audio_path)

def filter_text(text):
    text = text.replace("*", " ")
    return text


def text2Speech(spoken_text, language) -> None:
    # Initialize the converter
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # for index, voice in enumerate(voices):
    #     print(f"Voice {index}: {voice.name} - {voice.languages}")

    engine.setProperty('voice', voices[150].id)
    engine.setProperty('rate', 130)
    engine.say(spoken_text)
    engine.runAndWait()
    print("done converting spoken text to speech")
    pass


def text2Speech_elevenlabs(spoken_text, language) -> None:
    try:
        response = client.text_to_speech.convert(
            voice_id="pNInz6obpgDQGcFmaJgB",
            # optimize_streaming_latency="0",
            output_format="mp3_22050_32",
            text=spoken_text,
            model_id="eleven_turbo_v2_5",
            voice_settings=VoiceSettings(
                stability=0.0,
                similarity_boost=1.0,
                style=0.0,
                use_speaker_boost=True,
            ),
        )
        print(f"uuid.uuid4(), {uuid.uuid4()}")

        if not os.path.exists("./audio"):
            os.makedirs("./audio")
        audio_folder = "./audio"
        
        save_file_path = os.path.join(audio_folder, f"{uuid.uuid4()}.mp3")
        print("🐍 File: ai-asistant/assistant.py | Line: 81 | text2Speech_elevenlabs ~ save_file_path",save_file_path)

        # Writing the audio to a file
        with open(save_file_path, "wb") as f:
            for chunk in response:
                if chunk:
                    f.write(chunk)

        print(f"{save_file_path}: A new audio file was saved successfully!")

        # Return the path of the saved audio file
        return save_file_path
    
    except FileNotFoundError as e:
        print(e)

    except Exception as e:
        print(e)



def play_audio(file_path):
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue



chatfun()