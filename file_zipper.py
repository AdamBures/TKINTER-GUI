import tkinter as tk 
from tkinter import filedialog, messagebox
import os 
from zipfile import ZipFile 

win = tk.Tk()
win.resizable(False,False)
win.geometry("500x500")
win.title("Zipper")

def zip():
	pass

def unzip():
	pass

def zipbrowser():
	pass

def unzipbrowser():
	pass

zipvar = tk.StringVar()
unzipvar = tk.StringVar()

sel = tk.Label(win,text="Select file")
sel.grid(row=0, column=0)

select_entry = tk.Entry(win, textvariable=zipvar,width=30)
select_entry.grid(row=0,column=1)

btn = tk.Button(win, text="Open file to zip" ,command=zipbrowser)
btn.grid(row=0,column=2)


win.mainloop()