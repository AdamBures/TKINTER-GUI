from pytube import YouTube
import tkinter as tk
from tkinter import messagebox
import os
from moviepy.editor import *

win = tk.Tk()
win.resizable(False,False)
win.title("YouTube Downloader")
win.geometry("250x250")
v = tk.IntVar()
v.set(1)
def download():
	#try:
		if v.get() == 1:
			yt = YouTube(entry.get()).streams.get_highest_resolution().download()
			messagebox.showinfo("Download", f"Video is dowloaded {yt.title()}")
		else:
			yt = YouTube(entry.get()).streams.get_highest_resolution().download()
			video = VideoFileClip(os.path.join(f"{os.getcwd()}",f"{os.getcwd()}",f"{yt}"))
			video.audio.write_audiofile(os.path.join(f"{os.getcwd()}",f"{os.getcwd()}",f"{yt}.mp3"))
			messagebox.showinfo("Download", f"Video is dowloaded")

	#except:
	#	messagebox.showerror("ERROR", "Error has occured")


lbl = tk.Label(win,text="Download Youtube video").pack()
tk.Radiobutton(win, 
              text="MP4",
              padx = 20, 
              variable=v, 
              value=1).pack(anchor=tk.W)
tk.Radiobutton(win, 
              text="MP3",
              padx = 20, 
              variable=v, 
              value=2).pack(anchor=tk.W)
entry = tk.Entry(win)
entry.pack()
btn = tk.Button(win,text="Download",command=download).pack()
win.mainloop()