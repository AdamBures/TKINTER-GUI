import tkinter as tk

win = tk.Tk()
win.title("Calculator")
win.resizable(False,False)

def click(number):
	global operator
	operator = operator + str(number)
	variable.set(operator)

def clear():
	global operator
	operator = ""
	variable.set(operator)

def equal():
	global operator
	try:
		operator = str(eval(operator))
	except:
		entry.insert(0,"Error")
	finally:
		variable.set(operator)
operator = ""

variable = tk.StringVar()
entry = tk.Entry(win, font=("arial", 20, "bold"), textvariable=variable,justify="right")
entry.grid(columnspan=5)

button7 = tk.Button(win, text="7", font=("arial", 20, "bold"), bd=5, padx=10,command=lambda: click(7))
button7.grid(row=1,column=0)

button8 = tk.Button(win, text="8", font=("arial", 20, "bold"), bd=5, padx=10,command=lambda: click(8))
button8.grid(row=1,column=1)

button9 = tk.Button(win, text="9", font=("arial", 20, "bold"), bd=5, padx=10,command=lambda: click(9))
button9.grid(row=1,column=2)

button4 = tk.Button(win, text="4", font=("arial", 20, "bold"), bd=5, padx=10,command=lambda: click(4))
button4.grid(row=2,column=0)

button5 = tk.Button(win, text="5", font=("arial", 20, "bold"), bd=5, padx=10,command=lambda: click(5))
button5.grid(row=2,column=1)

button6 = tk.Button(win, text="6", font=("arial", 20, "bold"), bd=5, padx=10,command=lambda: click(6))
button6.grid(row=2,column=2)

button3 = tk.Button(win, text="3", font=("arial", 20, "bold"), bd=5, padx=10,command=lambda: click(3))
button3.grid(row=3,column=0)

button2 = tk.Button(win, text="2", font=("arial", 20, "bold"), bd=5, padx=10,command=lambda: click(2))
button2.grid(row=3,column=1)

button1 = tk.Button(win, text="1", font=("arial", 20, "bold"), bd=5, padx=10,command=lambda: click(1))
button1.grid(row=3,column=2)

button_divide = tk.Button(win, text="/", font=("arial", 20, "bold"), bd=5, padx=10,command=lambda: click("/"))
button_divide.grid(row = 1, column = 3)

button_sum = tk.Button(win, text="+", font=("arial", 20, "bold"), bd=5, padx=10,command=lambda: click("+"))
button_sum.grid(row=2, column= 3)

button_multi = tk.Button(win, text="*", font=("arial", 20, "bold"), bd=5, padx=10,command=lambda: click("*"))
button_multi.grid(row=3,column=3)

button_minus = tk.Button(win, text="-", font=("arial", 20, "bold"), bd=5, padx=10,command=lambda: click("-"))
button_minus.grid(row=4,column=3)

button_zero = tk.Button(win,text="0",font=("arial", 20, "bold"), bd=5, padx=10,command=lambda: click(0))
button_zero.grid(row=4, column=0)

button_point = tk.Button(win,text=".",font=("arial", 20, "bold"), bd=5, padx=10,command=lambda: click("."))
button_point.grid(row=4, column=1)

button_equal = tk.Button(win,text="=",font=("arial", 20, "bold"), bd=5, padx=10,command=equal)
button_equal.grid(row=4, column=2)

button_clear = tk.Button(win,text="C",font=("arial", 20, "bold"), bd=5, padx=10,command=clear)
button_clear.grid(row=4, column = 3)

win.mainloop()