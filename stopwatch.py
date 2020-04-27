from tkinter import *

run = True; s=0; m=0; h=0

def Run():
    global run, s, m, h

    # Delete old text
    w.delete('all')
    # Add new text
    w.create_text(
        [125, 75], anchor=CENTER, text="%s:%s:%s" % (h,m,s), font=("Consolas", 50)
        )

    s+=1
    if s == 59:
        m+=1; s=-1
    elif m == 59:
        h+=1; m=-1

    # After 1 second, call Run again (start an infinite recursive loop)
    master.after(1000, Run)

master = Tk()
w = Canvas(master, width=250, height=150)
w.pack()

master.after(1, Run)  # after 1 millisecond, start Run
mainloop()