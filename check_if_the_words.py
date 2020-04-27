import language_check
import tkinter as tk
from tkinter import filedialog

win = tk.Tk()
win.geometry("250x100")
win.resizable(False,False)
win.title("Check for mistakes")

def check():
	tool = language_check.LanguageTool("en-US")
	text = open(name, "r+")
	a = text.read()
	matches = tool.check(a)
	number_of_mistakes = len(matches)
	b = language_check.correct(text, matches)
	text_reopen = open(name, "w")
	text_reopen.write(b)
	fin_text = "File has corrected number of mistakes or typos is {}".format(number_of_mistakes)
	label1 = tk.Label(win, text=fin_text, font=("arial", 11, "bold"))
	label1.grid(row=2, column= 0)
	win.geometry("250x200")

	print(fin_text)

def open_file():
	global name
	name = filedialog.askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                           filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    #Using try in case user types in unknown file or closes without choosing a file.
    


label = tk.Label(win, text="Enter filename:", font=("arial", 11, "bold"))
label.grid(row=0, column= 0)

button = tk.Button(win, text="Open",command=open_file)
button.grid(row=1,column=0)

button1 = tk.Button(win, text="Check",command=check)
button1.grid(row=1,column=1)

win.mainloop()