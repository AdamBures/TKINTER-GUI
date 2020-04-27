import tkinter as tk
from gtts import gTTS
from playsound import playsound
import random
import os


win = tk.Tk()
win.title("Text2Speech")
win.geometry("400x70")

def play():
    num = random.randint(1, 999)
    text = entry.get()
    ftext = text + str(num)
    speech = gTTS(text=text, lang="cs")
    speech.save(r"{}.mp3".format(ftext))
    playsound(r"{}.mp3".format(ftext), True)
    os.remove(r"{}.mp3".format(ftext))
    


label = tk.Label(win, text="Enter message to read")
label.grid(column=0, row=0)

entry = tk.Entry(win)
entry.grid(column=0, row=1)

butt = tk.Button(win, text="Pass", command=play)
butt.grid(column=1, row=1)

win.mainloop()
