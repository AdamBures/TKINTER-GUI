import calendar
import tkinter

win = tkinter.Tk()
win.title("Calendar")

def text():
    month = int(entry.get())
    year = int(entry1.get())
    cal = calendar.month(year, month)
    textfield.delete(0.0, tkinter.END)
    textfield.insert(tkinter.INSERT,cal)

label = tkinter.Label(win, text="Month: ")
label.grid(row=0, column=0)

label1 = tkinter.Label(win, text="Year: ")
label1.grid(row=0, column=1)

entry = tkinter.Spinbox(win, from_=1, to=12, width=5)
entry.grid(row=1, column=0)

entry1 = tkinter.Spinbox(win, from_=1, to=9999, width=5)
entry1.grid(row=1, column=1)

but = tkinter.Button(win, text="Go", command=text)
but.grid(row= 1, column=2)

textfield = tkinter.Text(win, height=10, width=25, foreground="red")
textfield.grid(row=3, columnspan=3)

win.resizable(0,0)

win.mainloop()
