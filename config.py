import os 

from dotenv import load_dotenv
load_dotenv()

ELEVEN_LABS_API_KEY = os.environ.get('ELEVENLABS_API_KEY')
GOOGLE_SPEECH_RECOGNITION_API_KEY = os.environ.get('GOOGLE_SPEECH_RECOGNITION_API_KEY') # api key