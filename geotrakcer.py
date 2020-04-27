import tkinter as tk
import geocoder

win = tk.Tk()
win.geometry("300x85")
win.title("Geotracker")
win.resizable(False,False)

def get_langtitude():
	user_input = entry.get()
	latlng_info = geocoder.ip(user_input)
	location = str(geocoder.ip(user_input))
	win.geometry("400x100")
	label2 = tk.Label(win, text="The location is {0}".format(location[23:46]))
	label2.grid(row=2,column=0)
	label3 = tk.Label(win, text="The location is {0}".format(latlng_info.latlng))
	label3.grid(row=3,column=0)
		


label = tk.Label(win, text="Enter your ip adress")
label.grid(row=0, column= 0)

entry = tk.Entry(win)
entry.grid(row=1,column=0)

but = tk.Button(win, text="Press here", command = get_langtitude)
but.grid(row=1, column=1)

win.mainloop()