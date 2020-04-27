from tkinter import *

from tkinter import ttk
from time import ctime
import time
import speech_recognition as sr
import pyaudio
import webbrowser
import os
import playsound
import random
from gtts import gTTS
        
def speak(audio_string):
    tts = gTTS(text=audio_string, lang="en")

    number = random.randint(1, 10000000000)
    audio_file = "audio" + str(number) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)

def record_audio(ask=False):
    record = sr.Recognizer()
    with sr.Microphone() as source:
        if ask:
            speak(ask)

            audio = record.listen(source)
            voice_data = ""
        try:
            audio = record.listen(source)
            voice_data = record.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Did not get that")
        except sr.RequestError:
            speak("Server is down")

        return voice_data

def respond(voice_data):        
    if "name" in voice_data:
        speak("hi, my name is Rudolph. I'm your personal assistant")
    if "current time" in voice_data:
        speak(ctime())
    if "search" in voice_data:
        search = record_audio("What do you want to search")
        url = 'https://google.com/search?q='+ str(search)
        webbrowser.get().open(url)
        speak(f"Here is what I have found {search}")
    if "find location" in voice_data:
        location = record_audio("Which you want to like to go ? ")
        url = 'https://google.nl/maps/place'+ str(location)
        webbrowser.get().open(url)
        speak("here is your location"+str(location)+'/&amp;')
    if "exit" in voice_data:
        speak("Goodbye have a nice day")
        sys.exit()
    
def task():
    speak("How can i help you")
    voice_data = record_audio()
    respond(voice_data)

root = Tk()
root.resizable(False,False)
root.title("Voice Assistant")





task_btn = Button(root,text="Command", width=10,command=task).grid(row=0,column=0, ipady=20, ipadx=90)
exit_btn = Button(root,text="Exit",width=10,command=root.destroy).grid(row=1,column=0, ipady=20, ipadx=90)

root.mainloop()