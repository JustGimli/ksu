from email.mime import audio
import speech_recognition as speech


print(speech.Microphone.list_microphone_names())

# def get_audio():
#     global rec,mic

#     rec = speech.Recognizer()
#     mic = speech.Microphone()


#     while True:
#         voice_input = record_recognize_audio()
#         # print(voice_input)
    
# def record_recognize_audio(*args):
#     with mic as audio_file:

#         rec.adjust_for_ambient_noise(mic,duration=5)

#         audio = rec.listen(audio_file)
#         print(rec.recognize_google(audio))
        
# get_audio()