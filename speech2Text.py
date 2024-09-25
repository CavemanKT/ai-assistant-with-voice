import speech_recognition as sr

from config import GOOGLE_SPEECH_RECOGNITION_API_KEY
def record_voice(language="en-US") -> str:
    # r = sr.Recognizer(language = "en-US", key=GOOGLE_SPEECH_RECOGNITION_API_KEY)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        print("Done recording")
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand your audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

