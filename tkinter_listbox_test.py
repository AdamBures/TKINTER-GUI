import tkinter as tk

string = "Hello Listbox"

win = tk.Tk()
win.geometry("250x250")
win.resizable(False,False)

lstbox = tk.Text(win)
lstbox.insert(tk.END,string)
lstbox.pack()


win.mainloop()