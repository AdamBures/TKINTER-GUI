import ctypes
import tkinter as tk
from tkinter import filedialog


win = tk.Tk()
win.resizable(False,False)
win.geometry("325x50")
win.title("Wallpaper changer")

def open_file():
	global name
	name = filedialog.askopenfilename(initialdir="C:/Desktop",
                           filetypes =(("PNG", "*.png"),("JPG", "*jpg"), ("JPEG", "*jpeg"), ("All Files","*.*")),
                           title = "Choose a file."
                           )

def change_wall():
	open_file()
	ctypes.windll.user32.SystemParametersInfoW(20, 0, name , 0)



tk.Label(win,text="Click the button and select the wallpaper you want to use").pack()
tk.Button(win, text="Open a file", command=change_wall, width=45).pack()

win.mainloop()