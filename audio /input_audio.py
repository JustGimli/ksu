from email.mime import audio
import speech_recognition as speech
from vosk import KaldiRecognizer,Model

# print(speech.Microphone.list_microphone_names())

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

        rec.adjust_for_ambient_noise(mic,duration=5)
        try:
            print('listening')
            audio = rec.listen(audio_file,5,5)
            
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
            
        
        return recg_data
        
get_audio()