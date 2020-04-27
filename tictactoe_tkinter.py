import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("535x600")
root.resizable(False,False)
root.configure(background="powder blue")
buttons = tk.StringVar()
i = 1

def checker(buttons):
	global i
	if buttons["text"] == " " and i == 1:
		buttons["text"] = "X"
		i += 1
		winner()
	elif buttons["text"] == " " and i == 2:
		buttons["text"] = "O"
		i -= 1
		winner()
flag = 1
def winner():
	global flag
	if (btn1["text"]== "X" and btn2["text"] == "X"and btn3["text"] == "X"):
		btn1.configure(background="powder blue")
		btn2.configure(background="powder blue")
		btn3.configure(background="powder blue")

		messagebox.showinfo("WINNER IS X", "WINNER IS X")

	elif (btn4["text"]== "X" and btn5["text"] == "X"and btn6["text"] == "X"):
		btn4.configure(background="powder blue")
		btn5.configure(background="powder blue")
		btn6.configure(background="powder blue")

		messagebox.showinfo("WINNER IS X", "WINNER IS X")


	elif (btn7["text"]== "X" and btn8["text"] == "X"and btn9["text"] == "X"):
		btn7.configure(background="powder blue")
		btn8.configure(background="powder blue")
		btn9.configure(background="powder blue")

		messagebox.showinfo("WINNER IS X", "WINNER IS X")

	elif (btn1["text"]== "X" and btn5["text"] == "X"and btn9["text"] == "X"):
		btn1.configure(background="powder blue")
		btn5.configure(background="powder blue")
		btn9.configure(background="powder blue")

		messagebox.showinfo("WINNER IS X", "WINNER IS X")

	elif (btn3["text"]== "X" and btn5["text"] == "X"and btn7["text"] == "X"):
		btn3.configure(background="powder blue")
		btn5.configure(background="powder blue")
		btn7.configure(background="powder blue")

		messagebox.showinfo("WINNER IS X", "WINNER IS X")

	elif (btn1["text"]== "X" and btn4["text"] == "X"and btn7["text"] == "X"):
		btn1.configure(background="powder blue")
		btn4.configure(background="powder blue")
		btn7.configure(background="powder blue")

		messagebox.showinfo("WINNER IS X", "WINNER IS X")

	elif (btn2["text"]== "X" and btn5["text"] == "X"and btn8["text"] == "X"):
		btn2.configure(background="powder blue")
		btn5.configure(background="powder blue")
		btn8.configure(background="powder blue")

		messagebox.showinfo("WINNER IS X", "WINNER IS X")

	elif (btn3["text"]== "X" and btn6["text"] == "X"and btn9["text"] == "X"):
		btn3.configure(background="powder blue")
		btn6.configure(background="powder blue")
		btn9.configure(background="powder blue")

		messagebox.showinfo("WINNER IS X", "WINNER IS X")
	#########################################################

	elif (btn1["text"]== "O" and btn2["text"] == "O"and btn3["text"] == "O"):
		btn1.configure(background="powder blue")
		btn2.configure(background="powder blue")
		btn3.configure(background="powder blue")

		messagebox.showinfo("WINNER IS O", "WINNER IS O")

	elif (btn4["text"]== "O" and btn5["text"] == "O"and btn6["text"] == "O"):
		btn4.configure(background="powder blue")
		btn5.configure(background="powder blue")
		btn6.configure(background="powder blue")

		messagebox.showinfo("WINNER IS O", "WINNER IS O")


	elif (btn7["text"]== "O" and btn8["text"] == "O"and btn9["text"] == "O"):
		btn7.configure(background="powder blue")
		btn8.configure(background="powder blue")
		btn9.configure(background="powder blue")

		messagebox.showinfo("WINNER IS O", "WINNER IS O")

	elif (btn1["text"]== "O" and btn5["text"] == "O"and btn9["text"] == "O"):
		btn1.configure(background="powder blue")
		btn5.configure(background="powder blue")
		btn9.configure(background="powder blue")

		messagebox.showinfo("WINNER IS O", "WINNER IS O")

	elif (btn3["text"]== "O" and btn5["text"] == "O"and btn7["text"] == "O"):
		btn3.configure(background="powder blue")
		btn5.configure(background="powder blue")
		btn7.configure(background="powder blue")

		messagebox.showinfo("WINNER IS O", "WINNER IS O")

	elif (btn1["text"]== "O" and btn4["text"] == "O"and btn7["text"] == "O"):
		btn1.configure(background="powder blue")
		btn4.configure(background="powder blue")
		btn7.configure(background="powder blue")

		messagebox.showinfo("WINNER IS O", "WINNER IS O")

	elif (btn2["text"]== "O" and btn5["text"] == "O"and btn8["text"] == "O"):
		btn2.configure(background="powder blue")
		btn5.configure(background="powder blue")
		btn8.configure(background="powder blue")

		messagebox.showinfo("WINNER IS O", "WINNER IS O")

	elif (btn3["text"]== "O" and btn6["text"] == "O"and btn9["text"] == "O"):
		btn3.configure(background="powder blue")
		btn6.configure(background="powder blue")
		btn9.configure(background="powder blue")

		messagebox.showinfo("WINNER IS O", "WINNER IS O")


def reset():
	btn1["text"]= " "
	btn2["text"]= " "
	btn3["text"]= " "
	btn4["text"]= " "
	btn5["text"]= " "
	btn6["text"]= " "
	btn7["text"]= " "
	btn8["text"]= " "
	btn9["text"]= " "

	btn1.configure(background="gainsboro")
	btn2.configure(background="gainsboro")
	btn3.configure(background="gainsboro")
	btn4.configure(background="gainsboro")
	btn5.configure(background="gainsboro")
	btn6.configure(background="gainsboro")
	btn7.configure(background="gainsboro")
	btn8.configure(background="gainsboro")
	btn9.configure(background="gainsboro")


mainframe = tk.Frame(root,height=450,width=600).place()
btn1 = tk.Button(mainframe,text = " ", font = ("times", 26, "bold"), height= 3,width= 8, bg="gainsboro", command = lambda: checker(btn1))
btn1.grid(row= 1, column = 1)

btn2 = tk.Button(mainframe,text = " ", font = ("times", 26, "bold"), height= 3,width= 8, bg="gainsboro", command = lambda: checker(btn2))
btn2.grid(row= 1, column = 2)

btn3 = tk.Button(mainframe,text = " ", font = ("times", 26, "bold"), height= 3,width= 8, bg="gainsboro", command = lambda: checker(btn3))
btn3.grid(row= 1, column = 3)

btn4 = tk.Button(mainframe,text = " ", font = ("times", 26, "bold"), height= 3,width= 8, bg="gainsboro", command = lambda: checker(btn4))
btn4.grid(row= 2, column = 1)

btn5 = tk.Button(mainframe,text = " ", font = ("times", 26, "bold"), height= 3,width= 8, bg="gainsboro", command = lambda: checker(btn5))
btn5.grid(row= 2, column = 2)

btn6 = tk.Button(mainframe,text = " ", font = ("times", 26, "bold"), height= 3,width= 8, bg="gainsboro", command = lambda: checker(btn6))
btn6.grid(row= 2, column = 3)

btn7 = tk.Button(mainframe,text = " ", font = ("times", 26, "bold"), height= 3,width= 8, bg="gainsboro", command = lambda: checker(btn7))
btn7.grid(row= 3, column = 1)

btn8 = tk.Button(mainframe,text = " ", font = ("times", 26, "bold"), height= 3,width= 8, bg="gainsboro", command = lambda: checker(btn8))
btn8.grid(row= 3, column = 2)

btn9 = tk.Button(mainframe,text = " ", font = ("times", 26, "bold"), height= 3,width= 8, bg="gainsboro", command = lambda: checker(btn9))
btn9.grid(row= 3, column = 3)

btn_reset = tk.Button(mainframe, text="RESET", font = ("times", 15, "bold"),height= 2,width= 20, bg="gainsboro", command = reset)
btn_reset.place(x=120,y=500)
root.mainloop()