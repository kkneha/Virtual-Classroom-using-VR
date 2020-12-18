import speech_recognition as sr
import os

global obj_no 

def recognise_model():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("say something...")
            r.adjust_for_ambient_noise(source)
            audio_data = r.listen(source)
            try:
                text = r.recognize_google(audio_data)
                if text == "exit":
                    break
                else:
                    print("in else")
                    obj_no = identify_object(text)
                    #print(text)
            except:
                print('Internet connectivity issue')
                
        break
    return obj_no

def identify_object(text):
    print("identifying", text)
    for i in text.split():
        print (i)
        if i == "cube":
            obj_no = 0
            break
        if i == "sphere":
            obj_no = 1
            break
        if i == "cylinder":
            obj_no = 2
            break
    print(obj_no)
    return obj_no


