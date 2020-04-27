import tkinter as tk
import os
import base64
import smtplib
import random
import time
import re
import sys
from tkinter import messagebox
from twilio.request import Client 

def register_window():
    global entry_username_register
    global email_entry_register
    global password_entry_register

    win = tk.Tk()
    win.resizable(False,False)
    win.title("Registration")
    win.geometry("250x250")
    
    lbl_title_register = tk.Label(win,text="Fill in the columns:").pack()
    lbl_username_register = tk.Label(win,text="Username:").pack()
    entry_username_register = tk.Entry(win)
    entry_username_register.pack()
    lbl_email = tk.Label(win,text="Email:").pack()
    email_entry_register = tk.Entry(win)
    email_entry_register.pack()
    lbl_password_register = tk.Label(win,text="Password:").pack()
    password_entry_register = tk.Entry(win,show="*")
    password_entry_register.pack()
    register_btn = tk.Button(win,text="REGISTER",command=register).pack()
    
    win.mainloop()


def login_window():
    global entry_username
    global email_entry
    global password_entry
    win1 = tk.Tk()
    win1.resizable(False,False)
    win1.title("Login")
    win1.geometry("250x250")

    lbl_title = tk.Label(win1,text="Fill the columns:").pack()
    lbl_username = tk.Label(win1,text="Username:").pack()
    entry_username = tk.Entry(win1)
    entry_username.pack()
    lbl_email = tk.Label(win1,text="Email:").pack()
    email_entry = tk.Entry(win1)
    email_entry.pack()
    lbl_password = tk.Label(win1,text="Password:").pack()
    password_entry = tk.Entry(win1,show="*")
    password_entry.pack()
    login_btn = tk.Button(win1,text="LOGIN",command=login).pack()
    lbl_forgoted_password = tk.Label(win1,text="Forgoted password ?\n Click the button and have a new password").pack()
    btn_forgoted_password = tk.Button(win1,text="Forgoted password ?", command=restore_password).pack()
    win1.mainloop()

def main_window():
    global entry_username_register
    win3 = tk.Tk()
    win3.resizable(False,False)
    win3.title("Welcome")
    win3.geometry("500x200")


    username = entry_username_register.get()

    lbl_welcome = tk.Label(win3,text=f"Welcome in your system {username}",font=("Arial",15)).pack()

    button = tk.Button(win3,text="Send Email", command=sendmail_func,width=100,height=3).pack()
    button2 = tk.Button(win3,text="Settings",command=open_settings,width=100,height=3).pack()
    button3 = tk.Button(win3,text="Exit App",command=exit,width=100,height=3).pack()

    win3.mainloop()

def exit():
    sys.exit()

def sendmail_func():
    global email_entry_text
    win5 = tk.Tk()
    win5.title("Send email")
    win5.geometry("500x500")
    win5.resizable(False,False)

    email_entry_label = tk.Label(win5,text="Enter Email of user you wanna contact").pack()
    email_entry_text = tk.Entry(win5,width=30)
    email_entry_text.pack()
    email_button = tk.Button(win5,text="SEND", command=sendmail)

    win5.mainloop()

def sendmail():
    global email_entry_text
    global email_entry
    message = email_entry_text.get()
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("sasi12345677@gmail.com", "jwyhxnizhyeuupbu")

    subject = "This user has send you mail using "
    body = f"{email_entry_text}"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        "sasi12345677@gmail.com",
        email_entry.get(),
        msg
    )

    print("Email has been send")
    server.quit()

def open_settings():
    win4 = tk.Tk()
    win4.geometry("250x250")
    win4.title("USER SETTINGS")
    win4.resizable(False,False)

    change_password = tk.Label(win4,text="Change password",width=30).pack()
    change_password_button = tk.Button(win4,text="Change",width=30,command=open_password_change).pack()
    change_email = tk.Label(win4, text="Change EMAIL",width=30).pack()
    change_email_button = tk.Button(win4,text="Change",width=30,command=open_email_change).pack()
    exit_but = tk.Button(win4,text="EXIT",command=exit).pack()

    win4.mainloop()

def open_email_change():
    global change_email_enter
    win7 = tk.Tk()
    win7.geometry("250x250")
    win7.title("USER SETTINGS")
    win7.resizable(False,False)
    change_email_lbl = tk.Label(win7,text="Change password",width=30).pack()
    change_email_enter = tk.Enter(win7)
    change_email_enter.pack()
    change_email_btn = tk.Button(win7,text="CHANGE PASSWORD",command=change_email_command)


def restore_password():
    global telephone_number
    win8 = tk.Tk()
    win8.geometry("250x250")
    win8.title("USER SETTINGS")
    win8.resizable(False,False)

    telephone_number = tk.Entry(win8)
    telephone_number.pack()
    forgoted_password = tk.Button(win8,text="Forgoted password",command=forgoted_password_email)
    forgoted_password_telephone = tk.Button(win8,text="Forgoted password",command=forgoted_password_sms)

def change_email_command():
    global change_email_enter
    en_email = change_email_enter.get()
    list_of_dirs = os.listdir()
    if f"{username}.txt" in list_of_dirs:
        with open(f"{username}.txt", "w") as file:
            file.write(en_email)    
            file.close()
            messagebox.showinfo("SUCCES", "Change succesful")
            print("Change succesful")

def open_password_change():
    global change_password_enter
    win6 = tk.Tk()
    win6.geometry("250x250")
    win6.title("USER SETTINGS")
    win6.resizable(False,False)
    change_password_lbl = tk.Label(win6,text="Change password",width=30).pack()
    change_password_enter = tk.Enter(win6)
    change_password_enter.pack()
    change_password_btn = tk.Button(win6,text="CHANGE PASSWORD",command=change_password_command)

def change_password_command():
    global change_password_enter
    en_password = change_password_enter.get()
    list_of_dirs = os.listdir()
    if f"{username}.txt" in list_of_dirs:
        with open(f"{username}.txt", "w") as file:
            file.write(en_password)    
            file.close()
            messagebox.showinfo("SUCCES", "Change succesful")
            print("Change succesful")

def forgoted_password_sms():
    global telephone_number

    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]

    client = Client(account_sid,auth_token)
    list_of_dirs = os.listdir()
    if f"{username}.txt" in list_of_dirs:
        with open(f"{username}.txt", "r") as file:
            verify = file.read().splitlines()
            if email in verify:
                en_password = base64.b64encode(password.encode("utf-8")).decode("utf-8")
                client.messages.create(to=f"+{telephone_number}", 
                                   from_="+12023351278", 
                                   body=f"This is your {en_password}")



def forgoted_password_email():
    global entry_username
    global email_entry
    username = entry_username.get()
    email = email_entry.get()
    list_of_dirs = os.listdir()
    if f"{username}.txt" in list_of_dirs:
        with open(f"{username}.txt", "r") as file:
            verify = file.read().splitlines()
            if email in verify:
                en_password = base64.b64encode(password.encode("utf-8")).decode("utf-8")
                print(password)

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.ehlo()

                server.login("sasi12345677@gmail.com", "jwyhxnizhyeuupbu")

                subject = "Here is your recovered password"
                body = f"Here is your password: {en_password}"

                msg = f"Subject: {subject}\n\n{body}"

                server.sendmail(
                    "sasi12345677@gmail.com",
                    email,
                    msg
                )

                print("Email has been send")
                server.quit()


def welcome_email():
    username = entry_username_register.get()
    email = email_entry_register.get()
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

def login():
    global entry_username
    global email_entry
    global password_entry
    username = entry_username.get()
    email = email_entry.get()
    password = password_entry.get()
    en_password = base64.b64encode(password.encode("utf-8")).decode("utf-8")

    list_of_dirs = os.listdir()
    if f"{username}.txt" in list_of_dirs:
        with open(f"{username}.txt", "r") as file:
            verify = file.read().splitlines()
            if email in verify:
                if en_password in verify:
                    print("Succesfully logged in")
                    main_window()         
                else:
                    print("Wrong password")
            else:
                print("Wrong email")
                    
    else:
        print("User not found")

def register():
    username = entry_username_register.get()
    email = email_entry_register.get()
    password = password_entry_register.get()
    en_password = base64.b64encode(password.encode("utf-8")).decode("utf-8")
    flag = 0
    list_of_dirs = os.listdir()
    if f"{username}.txt" in list_of_dirs:
        print("Username already created")
    else:
        while True:   
            if (len(password)<8): 
                flag = -1
                break
            elif not re.search("[a-z]", password): 
                flag = -1
                break
            elif not re.search("[A-Z]", password): 
                flag = -1
                break
            elif not re.search("[0-9]", password): 
                flag = -1
                break
            
            elif re.search("\s", password): 
                flag = -1
                break
            else: 
                flag = 0
                print("Valid Password") 
                with open(f"{username}.txt", "w") as file:
                    file.write(username + "\n")
                    file.write(email + "\n")
                    file.write(en_password)    
                    file.close()
                    print("Registration succesful")
                    welcome_email()
                    main_window()
                    break

          
        if flag ==-1: 
            print("Not a Valid Password")


def Main():
    win2 = tk.Tk()
    win2.resizable(False,False)
    win2.title("Registration")
    win2.geometry("250x90")

    lbl = tk.Label(win2,text="Chooes what you want to do ?").pack()
    btn = tk.Button(win2,text="Login",command=login_window,width=30,height=1).pack()
    btn2 = tk.Button(win2,text="Register", command=register_window,width=30,height=1).pack()

    win2.mainloop()


#Main()
