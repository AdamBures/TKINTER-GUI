import wikipedia
import tkinter as tk
import time
import os

win = tk.Tk()
win.title("Wikipedia")
win.geometry("400x150")

def search():
    #try:
        result = wikipedia.page(entry.get())
        a = result.url
        result1 = wikipedia.search(result)[0]
        label1 = tk.Label(win, text=f"{a}\n")
        label1.grid(row=2, column=0)
        f = open(f"{result1}.txt", "w")
        f.writelines(wikipedia.summary(result))
        label2 = tk.Label(win, text="The content of the page is in the {0}".format(result1))
        label2.grid(row=3, column=0)
    #except:
        #label1 = tk.Label(win, text=f"Can't find your topic for creating url\n")
        #label1.grid(row=2, column=0)

label = tk.Label(win, text="Enter topic you are interested in")
label.grid(row=0, column=0)

entry = tk.Entry(win)
entry.grid(row=1, column=0)

but = tk.Button(win, text="Press here", command=search)
but.grid(row=1, column=1)

win.mainloop()
#user_input = str(input("Enter a topic what you are interested in: "))

#result = wikipedia.page(user_input)

#b = result.summary

#print(b)
#time.sleep(60)
