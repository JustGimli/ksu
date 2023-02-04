import speech_recognition as sr

from logic.ckeks import simple_cheks
from speech import text_to_speech
# logic press on button

def main():  # enabled 2 micro BAG
    r = sr.Recognizer()
    r.dynamic_energy_threshold = True
    # r.pause_threshold = 5 # when enabled 
    r.energy_threshold = 40

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source=source,) 
    
        while True:
            try:
                audio = r.listen(source=source, phrase_time_limit=3)
                text = r.recognize_google(audio_data=audio, language='ru').lower()
                if "ксюша" in text:
                    simple_cheks()
            except Exception as e:
                print(e)




if '__main__' == __name__:
    main()