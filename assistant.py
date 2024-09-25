import speech2Text
from ollama import chat

from gtts import gTTS
import os

import pyttsx3

def chatfun():
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
    text2Speech(spoken_text, 'en-US')



def text2Speech(spoken_text, language) -> None:
    # Initialize the converter
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for index, voice in enumerate(voices):
        print(f"Voice {index}: {voice.name} - {voice.languages}")

    engine.setProperty('voice', voices[150].id)
    engine.setProperty('rate', 130)
    engine.say(spoken_text)
    engine.runAndWait()
    print("done converting spoken text to speech")
    pass


chatfun()