import tkinter as tk



def login():
	pass

def login_verify():
	pass

def register_user():
	username_info = username.get()
	password_info = password.get()
	email_info = email.get()
	
	string = str(username.get())
	file_name = f"{username_info}.txt"

	with open(f"{string}.txt", "w+") as file:
		file.write(username.get() + "\n")
		file.write(password.get() + "\n")
		file.write(email.get())											
		file.close()											    
		print("registration succesful")
		print(type(username_info))										    

def register():
	global win1
	global username
	global password
	global email
	win1 = tk.Tk()
	win1.resizable(False, False)
	win1.geometry("300x250")
	win1.title("Login System")
	tk.Label(win1, text="Login system", height="2", width="30").pack()
	tk.Label(win1, text="Username").pack()
	username = tk.StringVar()
	password = tk.StringVar()
	email = tk.StringVar()
	usr_edit = tk.Entry(win1,textvariable=username).pack()
	tk.Label(win1, text="Password").pack()
	pass_edit = tk.Entry(win1,textvariable=password).pack()
	tk.Label(win1, text="Email").pack()
	email_edit = tk.Entry(win1,textvariable=email).pack()
	tk.Label(win1, text="")	
	tk.Button(win1,text="Enter", height="2", width="30", command = register_user).pack()


def main_screen():
	global win
	win = tk.Tk()
	win.resizable(False, False)
	win.geometry("300x250")
	win.title("Login System")
	tk.Label(text="Login system", height="2", width="30").pack()
	tk.Button(text="Register", height="2", width="30", command = register).pack()
	tk.Button(text="Login", height="2", width="30", command = login).pack()
		
	win.mainloop()

main_screen()
