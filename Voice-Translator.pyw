import speech_recognition as sr
import pyttsx3
from translate import Translator

def speak():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        rec.adjust_for_ambient_noise(source)
        audio = rec.listen(source)
        try:
            print("Recognizing...")
            global data
            data = rec.recognize_google(audio)
            print(data)
            Voice(data)
            return data
        except sr.UnknownValueError as e:
            print("Try Again...")

def Voice(x):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate',120)
    engine.say(x)
    engine.runAndWait()

speak()

translator= Translator(to_lang="spain")
translation = translator.translate(data)

Voice(translation)