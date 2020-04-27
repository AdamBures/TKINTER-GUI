import tkinter as tk
from tkinter import filedialog
import PyPDF2
from tkinter import messagebox
win = tk.Tk()
win.geometry("250x250")
win.title("PDF CONVERTER")
win.resizable(False,False)


def open_file():
		global name
		name = filedialog.askopenfilename(initialdir="C:/Desktop",
	                           filetypes =(("PDF",".pdf"), ("All Files","*.*")),
	                           title = "Choose a file."
	                           )

def convert_pdf():
	open_file()
	pdf_reader = PyPDF2.PdfFileReader(name,strict=False)
	page_obj = pdf_reader.getPage(0)
	page_obj.extractText()
	messagebox.showinfo("SUCCESS", "File converted succesfully")


lbl = tk.Label(win,text="Open pdf file to convert\n and then wait it will convert").pack()
btn = tk.Button(win,text="CONVERT",command=convert_pdf).pack()

win.mainloop()