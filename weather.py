import tkinter as tk 
import requests
import json 


win = tk.Tk()
win.title("Weather")
win.geometry("400x150")



def weather():
	location = entry.get()
	url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&APPID=1d87df38eeba8eaa5cbe3de5364f4380&units=metric"
	response = requests.get(url)
	res = response.json()
	if res["cod"] != "404":
		x = res["main"]
		temperature = x["temp"]
		pressure = x["pressure"] 
		humidity = x["humidity"]
		y = res["weather"]
		weather_description = y[0]["description"]
		label1 = tk.Label(win, text=f"Your current temperature in the city is {temperature}. \n"
								   f"Your current pressure in the city is {pressure}. \n"
								   f"Your current humidity in the city is {humidity}. \n"
								   f"Weather description is {weather_description}. \n")
		label1.grid(row=2, column=0)
	else:
		label2 = tk.Label(win, text="Enter correct city")
		label2.grid(row=2, column=0)

label = tk.Label(win, text="Enter city")
label.grid(row=0, column=0)

entry = tk.Entry(win)
entry.grid(row=1, column=0)

but = tk.Button(win, text="Press here", command=weather)
but.grid(row=1, column=1)

win.mainloop()