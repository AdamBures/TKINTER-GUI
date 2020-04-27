from PIL import Image
import tkinter as tk
from tkinter import filedialog 

win2 = tk.Tk()
win2.resizable(False,False)
win2.geometry("400x130")
win2.title("Image opener")

def open_file():
	global name
	name = filedialog.askopenfilename(initialdir="C:/Desktop",
                           filetypes =(("PNG", "*.png"),("JPG", "*jpg"), ("JPEG", "*jpeg"), ("All Files","*.*")),
                           title = "Choose a file."
                           )



def image_resizer():

	width = entry1.get()
	height = entry2.get()

	ext = ".jpg"

	image = Image.open(name)

	tkimage = image.resize(width, height)
	tkimage.save(f"{name}_copy{ext}")

entry_text = tk.IntVar()
entry1_text = tk.IntVar()
tk.Label(win2,text="Width").grid(row=0,column=1,sticky="w")
entry1 = tk.Entry(win2, textvariable=entry_text).grid(row=1,column=1,sticky="w")
tk.Label(win2,text="Height").grid(row=2,column=1,sticky="w")
entry2 = tk.Entry(win2, textvariable=entry1_text).grid(row=3,column=1,sticky="w")
tk.Button(win2, text="Open Image",command=open_file).grid(row=4,column=1,sticky="w")
tk.Button(win2, text="Resize", command=image_resizer, width=9).grid(row=5,column=1,sticky="w")

win2.mainloop()