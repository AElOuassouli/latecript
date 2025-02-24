from .speechmatics_handler import transcribe_audio
from .speechamatics_app import SpeechmaticsApp

SAMPLE_RATE = 44100
CHANNELS = 2

SPEECHMATICS_INPUT_LANG = "fr"
SPEECHMATICS_API_KEY = "Z7vyXpWqlVOxi2qoTdNbYSLNd8k4gqZb"
SPEECHMATICS_CONNECTION_URL = f"wss://eu2.rt.speechmatics.com/v2/{SPEECHMATICS_INPUT_LANG}"

DEVICE_INDEX = -1
CHUNK_SIZE = 1024

def main() -> None:
    SpeechmaticsApp().run()

        


