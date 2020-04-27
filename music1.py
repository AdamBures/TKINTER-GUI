from pygame import mixer
import tkinter as tk
from tkinter import filedialog


win = tk.Tk()
win.geometry("250x100")
win.title("Music player")
win.resizable(False,False)



def open_file():
	global name
	name = filedialog.askopenfilename(initialdir="C:/Desktop",
                           filetypes =(("MP3", "*.mp3"),("WAV", "*wav"),("All Files","*.*")),
                           title = "Choose a file."
                           )
def play():
	open_file()
	mixer.init()
	mixer.music.load(name)
	mixer.music.play()
def stop():
	mixer.music.stop()

def pause():
	mixer.music.pause()

def unpause():
	mixer.music.unpause()



#button_open = tk.Button(win, text="Open file", command=open_file).pack()
button_play = tk.Button(win, text="Play", command=play, width=45).pack()
stop_btn = tk.Button(win, text="stop", command=stop, width=45).pack()
pause_btn = tk.Button(win, text="Pause", command=pause, width=45).pack()
unpause_btn = tk.Button(win,text="Unpause", command=unpause, width=45).pack()

win.mainloop()