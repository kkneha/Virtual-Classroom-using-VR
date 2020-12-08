import speech_recognition as sr
import os

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio_data = r.listen(source)
        try:
            text = r.recognize_google(audio_data)
            if text == "exit":
                break
            else:
                print(text)
        except:
            print('Internet connectivity issue')