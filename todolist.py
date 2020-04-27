import tkinter as tk

win = tk.Tk()
win.title("TODO List")
win.geometry("300x500")
win.resizable(False,False)

def clear():
	global operator
	operatror = ""
	variable.set(operator)

def add_todo(action):
	global operator
	operator = "XD"
	lb.insert(END, operator)


operator = ""

variable = tk.StringVar()
a = tk.Entry(win, width=300).pack()
lb = tk.Listbox(win, width=300).pack()

button = tk.Button(win, text="Add" ,command=lambda: add_todo("XD")).pack()


win.mainloop()