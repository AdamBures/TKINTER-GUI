import random
import tkinter as tk

win = tk.Tk()
win.title("Password Generator")
win.geometry("150x200")
win.resizable(False,False)

def create_pass():
	alphabet = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
	length = ent.get()
	length_int = int(length)
	p = "".join(random.sample(alphabet,length_int))
	password_lbl = tk.Label(win,text=p).grid(row=4,column=0)

	print(p)

lbl = tk.Label(win, text="Create your Password").grid(row=0,column=0)
length_lbl = tk.Label(win, text="Enter length of password: ").grid(row=1,column=0)
ent = tk.Entry(win)
ent.grid(row=2, column=0)
btn = tk.Button(win,text="Create", command=create_pass).grid(row=3,column=0)

win.mainloop()