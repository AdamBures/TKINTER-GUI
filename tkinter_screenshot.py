import tkinter as tk 
from PIL import Image, ImageTk
import pyautogui
import datetime as dt 
import random 

win = tk.Tk()
win.title("Screenshoter")
win.geometry("250x250")
win.resizable(False,False)
win.imageLabel = tk.Label(win)

def take_screenshot():
	today = dt.date.today().strftime("%d")
	number = random.randint(1,1000)

	screeenshot = pyautogui.screenshot()
	screeenshot.save(f"C:/Users/sasi1/Desktop/screenshots/screeenshot{number}{today}.jpg")

lbl = tk.Label(win,text="Click the button and take screenshot").pack()
btn = tk.Button(win,text="Take screenshot", command=take_screenshot).pack()
win.mainloop()