from tkinter import*
from tkinter import ttk,messagebox
import speech_recognition as sr

win = Tk()
win.title("Voice-Notepad")
win.geometry("600x600")
win.config(bg="white")
# win.iconbitmap("icon.ico")

def full_screen(event):
    win.geometry("766x784+761+0")

def insert(event):
    win.resizable(False,False)
    recocnizer = sr.Recognizer()
    with sr.Microphone() as source:
        intro.config(text="Listening...")
        win.update()
        print("Listening....")
        recocnizer.adjust_for_ambient_noise(source)
        audio = recocnizer.listen(source)
        try:
            print("Recognizing....")
            data = recocnizer.recognize_google(audio)
            writter.insert(INSERT,data)
            intro.config(text="Done")
            win.update_idletasks()
            win.update()
            win.resizable(True,True)
            return data
        except sr.UnknownValueError as e:
            print("Not Understanding")
            intro.config(text="Try Again..")
    
         


intro = Label(text="",font=("Elephant",15),bg="white")
intro.pack()
writter = Text(win,height=40,width=75,font=("consolas",15))
writter.pack()
win.bind('<Control-f>',full_screen)
win.bind('<Escape>',insert)
win.mainloop()

