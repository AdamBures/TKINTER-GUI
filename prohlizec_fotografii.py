from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk

win = Tk()
#win.resizable(False,False)
win.geometry("400x600")
win.title("Image opener")
win.imageLabel = Label(win)
win.imageLabel.grid(row = 2, column=1)



def open_file():
	global name
	name = filedialog.askopenfilename(initialdir="C:/Desktop",
                           filetypes =(("PNG", "*.png"),("JPG", "*jpg"), ("JPEG", "*jpeg"), ("All Files","*.*")),
                           title = "Choose a file."
                           )



def set_picture():
	open_file()
	try:
		image = Image.open(name)
		image = image.resize((400,400), Image.ANTIALIAS)
		image = ImageTk.PhotoImage(image)
		win.imageLabel.config(image=image)
		win.imageLabel.photo = image
	except:
		print("Cannot open pic")





btn = Button(win, text="Open", command=set_picture)
btn.grid(row=1,column=1)


win.mainloop()