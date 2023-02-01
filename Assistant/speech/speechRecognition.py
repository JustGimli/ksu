import speech_recognition as sr
import mute_alsa


def get_text(): # on button
    r = sr.Recognizer()
    r.dynamic_energy_threshold = True
    # r.pause_threshold = 5 # when enabled 
    # r.energy_threshold = 17695

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source=source) 
        
        try:
            audio = r.listen(source=source, timeout=3)
            text = r.recognize_google(audio_data=audio, language='ru')

            return text
        except sr.WaitTimeoutError as e:
            print("You dont say something")
        except sr.UnknownValueError:
            print("you dont say something")
        except sr.RequestError:
            print("Count recognize from") # should use vosk model
     
    


