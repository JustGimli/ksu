import os

from gtts import gTTS
from playsound import playsound


def voise_speech(text)->None:
    tts = gTTS(text, lang="ru")
    tts.save("speech.mp3")
    playsound("speech.mp3")
    os.remove("speech.mp3")


