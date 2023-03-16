from tkinter import*
from tkinter import ttk,messagebox
import speech_recognition as sr

win = Tk()
win.geometry("500x600")

def insert():
    recocnizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recocnizer.adjust_for_ambient_noise(source)
        audio = recocnizer.listen(source)
        try:
            print("Recognizing....")
            data = recocnizer.recognize_google(audio)
            writter.insert(INSERT,data)
            return data
        except sr.UnknownValueError as e:
            print("Not Understanding")
    win.update()
         
btn = ttk.Button(win,text="Speak",command=insert)

writter = Text(win)
writter.pack()
# win.bind('<Escape>',insert)
win.mainloop()