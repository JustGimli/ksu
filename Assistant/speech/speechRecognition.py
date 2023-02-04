import speech_recognition as sr

def get_text(): # on button
    r = sr.Recognizer()
    r.dynamic_energy_threshold = True
    # r.pause_threshold = 5 # when enabled 
    r.energy_threshold = 40

    

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source=source,) 
        
        try:
            audio = r.listen(source=source, phrase_time_limit=3)
            text = r.recognize_google(audio_data=audio, language='ru')

            return text.lower()
        except sr.WaitTimeoutError as e:
            print("repet plese")
        except sr.UnknownValueError:
            print("you dont say something")
        except sr.RequestError:
            print("Count recognize from") # should use vosk model
     

