import tkinter as tk
import time


class MainWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("Time")
        self.create_widgets()

    def digital_clock(self):
        self.time1 = time.strftime("%H:%M:%S")
        self.current_time.config(text=self.time1)
        self.current_time.after(250, self.digit_clock)
    
    def create_widgets(self):
        self.digit_clock = tk.Label(text="Digital Clock", font=("arial", 25,"bold"))
        self.digit_clock.grid(row=0, column=0)

        self.current_time = tk.Label(font=("times new roman", 35, "bold"))
        self.current_time.grid(row=1,column=0,padx= 60, pady=30)
        self.digital_clock()

    
        
root = tk.Tk()
app = MainWindow(root)
app.mainloop()
