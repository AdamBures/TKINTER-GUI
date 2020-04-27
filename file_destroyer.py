import tkinter as tk
from tkinter import filedialog
import os

win = tk.Tk()
win.geometry("250x250")
win.title("File Destroyer")
win.resizable(False,False)

def open_file():
	global name
	name = filedialog.askopenfilename(initialdir=r"C:\Users\sasi1\Desktop",
                           filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                           title = "Choose a file."
                           )


def destroy_file():
	open_file()
	os.remove(name)
	win.geometry("350x350")
	lbl1 = tk.Label(win, text=f"File under name {name} was destroyed").pack()

lbl = tk.Label(win, text="Choose file to destroy").pack()
btn = tk.Button(win, text="Open file to destroy", command=destroy_file).pack()

win.mainloop()