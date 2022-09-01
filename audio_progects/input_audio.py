import re
import speech_recognition as speech
from vosk import KaldiRecognizer,Model
import wave
import json 
import os
# z

def get_audio():

    global rec,mic

    rec = speech.Recognizer()
    mic = speech.Microphone()


    while True:
        voice_input = record_recognize_audio()
        print(voice_input)
    
def record_recognize_audio(*args):

    with mic as audio_file:

        recg_data = ''

        rec.adjust_for_ambient_noise(mic,duration=3)
        try:
            print('listening')
            audio = rec.listen(audio_file,5,5)
            
            with open("microphone-results.wav", "wb") as file:
                file.write(audio.get_wav_data())        


        except speech.WaitTimeoutError:
            print('Проверьте микрофон')
            return 
        
        #online regognizing
        try:
            print('начало разпознования')
            recg_data = rec.recognize_google(audio,language='ru').lower()
        except speech.UnknownValueError:
            pass
        
        except speech.RequestError:
            print('net connection bad')
            use_offline_recognition()
            os.remove('microphone-results.wav')
            
        
        return recg_data


def use_offline_recognition():

    recognition_data = ''
    try: 
        wave_audio_file = wave.open('microphone-results.wav','rb')
        model = Model('./audio_progects/models/vosk-model-small-ru-0.22')
        offline_recognizer = KaldiRecognizer(model,16000)
        data = wave_audio_file.readframes(wave_audio_file.getnframes())

        if len(data) > 0:
            if  offline_recognizer.AcceptWaveform(data):
                recognition_data = offline_recognizer.Result()
                recognition_data = json.load(recognition_data)
                recognition_data = recognition_data['text']

    except:
        print('sorry,vpsk didnt work')    
    
    return recognition_data


get_audio() 