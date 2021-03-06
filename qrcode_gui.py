import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import qrcode

win = tk.Tk()
win.title("QR Code generator")
win.resizable(False,False)
win.geometry("500x450")
win.imageLabel = tk.Label(win)
win.imageLabel.grid(row = 2, column=1)

def GenerateQR():
	qrString = entry.get()

	if qrString != "":
		f = qrcode.make(qrString)

		f.save(f"C:/Users/sasi1/Desktop/Python projects/{qrString}.png")

		image = Image.open(f"{qrString}.png")
		image = image.resize((400,400), Image.ANTIALIAS)
		image = ImageTk.PhotoImage(image)
		win.imageLabel.config(image=image)
		win.imageLabel.photo = image

	else:
		messagebox.showerror("ERROR", "Enter text")

label = tk.Label(win, text="Enter text: ")
label.grid(row=0, column=0)

entry = tk.Entry(win)
entry.grid(row=0,column=1)

btn = tk.Button(win,text="Create QRCODE", command= GenerateQR)
btn.grid(row=1,column=1)


win.mainloop()