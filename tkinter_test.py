from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
window.title("First App")
window.geometry("650x200")

lbl1 = Label(window, text="This is Label", font=("Arial Bold", 50), bg= "red", fg="blue")
lbl1.grid(column=0, row=0)

txt = Entry(window,width=120)
txt.grid(column=1, row=0)

lbl1 = Label(window, text="Welcome to the Tkinter", font=("Arial Bold", 50), bg= "red", fg="blue")
lbl1.grid(column=1, row=1)

combo = Combobox(window)
combo["values"] = (1,2,3,4,5,6)
combo.grid(column=0, row=2)

lbl2 = Label(window, text="This is showcase of combobox", font=("Arial Bold", 50), bg= "red", fg="blue")
lbl2.grid(column=1, row=2)

def clicked():
    res = f"Welcome to the Tkinter {txt.get()}"
    
    lbl1.configure(text=res)

def check_current():
    res = f"You have chose the {combo.get()}"

    lbl2.configure(text=res)

btn = Button(window, text="This is Button", font=("Arial Bold", 25), bg= "orange", fg="red", width=10, command=clicked)
btn.grid(column=2, row=0)

btn = Button(window, text="Show me value in combobox", font=("Arial Bold", 25), bg= "orange", fg="red", width=25, command=check_current)
btn.grid(column=2, row=2)



window.mainloop()

