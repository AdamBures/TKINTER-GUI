import tkinter as tk
import os
import base64
import smtplib
import random
import time

class Login:
    def __init__(self, username,email,password):
        self.username = username
        self.email = email
        self.password = password

    def welcome_email(username,email):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login("sasi12345677@gmail.com", "jwyhxnizhyeuupbu")

        subject = "Welcome in our great login system"
        body = f"You are now registered inside are greatest database under username {username}"

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            "sasi12345677@gmail.com",
            email,
            msg
        )

        print("Email has been send")
        server.quit()

    def register(username,email, password):
        password = base64.b64encode(password.encode("utf-8")).decode("utf-8")

        with open(f"{username}.txt", "w") as file:
            file.write(username + "\n")
            file.write(email + "\n")
            file.write(password)
            file.close()
            print("Registration succesful")
            Login.welcome_email(username,email)

    def forgoted_password(username, email):
        list_of_dirs = os.listdir()
        if f"{username}.txt" in list_of_dirs:
            with open(f"{username}.txt", "r") as file:
                verify = file.read().splitlines()
                if email in verify:
                    print(password)

                    server = smtplib.SMTP("smtp.gmail.com", 587)
                    server.ehlo()
                    server.starttls()
                    server.ehlo()

                    server.login("sasi12345677@gmail.com", "jwyhxnizhyeuupbu")

                    subject = "Here is your recovered password"
                    body = f"Here is your password: {password}"

                    msg = f"Subject: {subject}\n\n{body}"

                    server.sendmail(
                        "sasi12345677@gmail.com",
                        email,
                        msg
                    )

                    print("Email has been send")
                    server.quit()

    def login():
        username = username_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        password = base64.b64encode(password.encode("utf-8")).decode("utf-8")

        list_of_dirs = os.listdir()
        if f"{username}.txt" in list_of_dirs:
            with open(f"{username}.txt", "r") as file:
                verify = file.read().splitlines()
                if email in verify:
                    if password in verify:
                        print("Succesfully logged in")
                        
                    else:
                        print("Wrong password")
                        

                else:
                    print("Wrong email")
                    
        else:
            print("User not found")
            

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        lbl = tk.Label(parent,text="Welcome in my Login/Register SYSTEM\n choose what you want to do").pack()
        btn_login = tk.Button(parent, text="LOGIN",width=30,command=MainApplication.LoginWindow).pack()
        btn_register = tk.Button(parent,text="REGISTER",width=30,command=MainApplication.RegisterWindow).pack()


    def LoginWindow():
        global username_entry
        global email_entry
        global password_entry
        win = tk.Tk()
        win.resizable(False,False)
        win.title("LOGIN")
        win.geometry("250x250")

        lbl_username = tk.Label(win,text="Username:").pack()
        username_entry = tk.Entry(win)
        username_entry.pack()

        lbl_email = tk.Label(win, text="Email:").pack()
        email_entry = tk.Entry(win)
        email_entry.pack()

        lbl_password = tk.Label(win,text="Password:").pack()
        password_entry = tk.Entry(win)
        password_entry.pack()

        login_btn = tk.Button(win,text="Login", command=Login.login() ,width=30).pack()

    
    def RegisterWindow():
        pass


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("250x100")
    root.title("Login SYSTEM")
    root.resizable(False,False)
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
