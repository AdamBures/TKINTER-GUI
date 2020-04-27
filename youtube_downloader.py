import tkinter as tk
import webbrowser

win = tk.Tk()
win.resizable(False,False)
win.geometry("250x100")
win.title("Youtube downloader")
def downloader():
	url = entry.get()

	url = url[:12] + "ss" + url[12:]
	webbrowser.open(url)

label = tk.Label(win, text="Enter url to download video")
label.grid(row=0, column=0)

entry = tk.Entry(win)
entry.grid(row=1,column=0)

btn = tk.Button(win,text="Download", command=downloader)
btn.grid(row=2,column=0)


win.mainloop()