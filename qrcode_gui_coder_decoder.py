import tkinter as tk
from tkinter import messagebox,filedialog
from PIL import Image, ImageTk
from pyzbar import pyzbar

def encode():
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

def decode():
	win = tk.Tk()
	win.title("QR Code generator")
	win.resizable(False,False)
	win.geometry("500x450")
	win.imageLabel = tk.Label(win)
	win.imageLabel.grid(row = 2, column=1)

	def open_file():
		global name
		name = filedialog.askopenfilename(initialdir="C:/Desktop",
	                           filetypes =(("PNG", "*.png"),("JPG", "*jpg"), ("JPEG", "*jpeg"), ("All Files","*.*")),
	                           title = "Choose a file."
	                           )

	def Decode():
		open_file()
		d = pyzbar.decode(Image.open(name))
		data1 = d[0].data.decode("utf-8")
		
		if data1:
			messagebox.showinfo("Result", f"{data1}")
		else:
			messagebox.showerror("ERROR", f"{error}")


	lbl = tk.Label(win,text="Click the button to decode your QRCODE")
	lbl.grid(row=0,column=0)

	btn = tk.Button(win,text="Press to open", command=Decode).grid(row=1,column=0)


	win.mainloop()


def Main():
	win = tk.Tk()
	win.geometry("250x200")
	win.resizable(False,False)
	win.title("QRCODE generator")

	lbl = tk.Label(win,text="Click the button to proceed").grid(row=0,column=0)

	btn1 = tk.Button(win,text="Encode", command=encode,width=30).grid(row=1,column=0)
	btn2 = tk.Button(win,text="Decode", command=decode,width=30).grid(row=2,column=0)

	win.mainloop()

Main()