from tkinter import *
import sys


class Question1:
	def click_me():
	   if i.get() == "1939":
	   	print("Right")


	global i
	global root
	root = Tk()

	i = StringVar()
	Label(root,text="When did WW2 started ?").pack()
	r1 = Radiobutton(root, text="1945", value="1945", variable=i)
	r2 = Radiobutton(root, text="1939", value="1939",  variable=i)
	r3 = Radiobutton(root,text="1942",value="1942",variable=i).pack()
	r1.pack()
	r2.pack()



	button = Button(root, text="check", command=click_me)
	button.pack()
	root.geometry("300x300+120+120")
	root.mainloop()

class Question2:
	def click_me():
	   if i.get() == "Adolf Hitler":
	   	print("Right")

	global i
	root = Tk()

	i = StringVar()
	Label(root,text="Who was chancellor in germany before WW2").pack()
	r1 = Radiobutton(root, text="Adolf Hitler", value="Adolf Hitler", variable=i)
	r2 = Radiobutton(root, text="John Wick", value="John Wick",  variable=i)
	r3 = Radiobutton(root,text="Thanos",value="Thanos",variable=i).pack()
	r1.pack()
	r2.pack()



	button = Button(root, text="check", command=click_me)
	button.pack()
	root.geometry("300x300+120+120")
	root.mainloop()


def Main():
	win = Tk()
	win.title("Quiz game")
	win.geometry("250x45")
	win.resizable(False,False)
	Label(win,text="WELCOME IN QUIZ GAME", width=45).pack()
	Button(win, text="START", command=Question1, width=45).pack()

Main()

