import tkinter as tk
from tkinter import messagebox
import random
import time
import pygame

win = tk.Tk()
win.geometry("250x370")
win.title("Ricardo Lover")
win.resizable(False,False)


def calc_love():
	number = random.randint(60,120)
	messagebox.showinfo("LOVE", f"{entry.get()} Ricardo loves you on {number}%")

def play_music():
	pygame.init()
	pygame.mixer.init()
	sound = pygame.mixer.Sound("C:/Users/sasi1/Documents/Audacity/ugotthat.wav")
	sound.set_volume(0.05)   # Now plays at 90% of full volume.
	sound.play()

canvas = tk.Canvas(win)
canvas.pack()
gif1 = tk.PhotoImage(file="C:/Users/sasi1/Desktop/ricardo.gif", format="gif -index 2")
canvas.create_image(50,10,image=gif1, anchor="n")
lbl = tk.Label(win, text="Your name: ").pack()
entry = tk.Entry(win)
entry.pack()
btn = tk.Button(win, text="Calculate", command=calc_love).pack()
photo = tk.PhotoImage(file='C:/Users/sasi1/Downloads/play.png')
sound_btn = tk.Button(win, image=photo, command=play_music).pack(anchor="se")


win.mainloop()