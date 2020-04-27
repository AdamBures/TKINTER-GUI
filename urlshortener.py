import urllib.request
import tkinter as tk
import pyperclip as pc

win = tk.Tk()
win.geometry("300x100")
win.resizable(False, False)
win.title("Tiny url")

def tiny_url():
	global better
	url = entry.get()
	tiny_url_api = 'http://tinyurl.com/api-create.php?url='
	url = urllib.request.urlopen(tiny_url_api+url).read()
	better = url.decode("utf-8")
	win.geometry("450x100")
	label2 = tk.Label(win, text="The content of the page is in the {0}".format(better))
	label2.grid(row=2,column=0)

def copy_url():
	copy_of_url = pc.copy(better)


label = tk.Label(win, text="Enter an url you want to short")
label.grid(row=0, column=0)

entry = tk.Entry(win)
entry.grid(row=1, column=0)

but = tk.Button(win, text="Press here", command = tiny_url)
but.grid(row=1, column=1)

but_2 = tk.Button(win, text="COPY", command = copy_url)
but_2.grid(row=1, column=2)


win.mainloop()