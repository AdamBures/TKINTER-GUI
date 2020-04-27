import tkinter as tk
import requests
from bs4 import BeautifulSoup
import json, requests,urllib.request
from PIL import Image, ImageTk
import re


win = tk.Tk()
win.title("Downloader")
win.resizable(False,False)
win.geometry("500x600")

insta_id = tk.StringVar()
dwl_text= tk.StringVar()

def Downloader():
    download_path = r"C:\Users\sasi1\Desktop\Python projects"
    insta_username = insta_id.get()
    # Concatenating user-input instagram id with Instagram URL & storing complete URL in insta_url
    insta_url = "https://www.instagram.com/"+insta_username
    # Sending request to the insta_url URL & storing the response in insta_response
    insta_response =  requests.get(insta_url)
    # Specifying the desired format of the insta_Comments using html.parser
    # html.parser allows Python to read the components of the insta_Page
    soup = BeautifulSoup(insta_response.text, 'html.parser')
    # Finding <script> whose text matches with 'window._sharedData' using re.compile()
    script = soup.find('script', text=re.compile('window._sharedData'))
    # Splitting the text of <script>, 1 time at '=' and fetching the item at index 1
    # followed by removing the ';' from the string and storing the resulting string in page_json
    page_json = script.text.split(' = ', 1)[1].rstrip(';')
    # Parsing the above json page_json string using json_loads() and storing the resulting
    # dictionary in data variable which is a very long dictionary consisting of 19 items
    data = json.loads(page_json)

    # The profile_pic_url is present in value of key 'entry_data' which itself is a dictionary
    dp_url = data['entry_data']['ProfilePage'][0]['graphql']['user']['profile_pic_url_hd']
    # Concatenating download_path with user-input username & .jpg extension & storing it as dp name
    dp_name = download_path+"/"+insta_username+'.jpg'
    # Download the profile_pic from dp_url and saving under 'dp_name':
    urllib.request.urlretrieve(dp_url, dp_name)
    # Opening the dp_name image using the open() method of the Image module
    dp_image = Image.open(dp_name)
    # Resizing the image using Image.resize()
    dp_image = dp_image.resize((200, 200), Image.ANTIALIAS)
    # Creating object of PhotoImage() class to display the frame
    image = ImageTk.PhotoImage(dp_image)

    win.dbpLabel.config(image=image)
    win.dbpLabel.photo = image
    dwl_text.set("DP DOWNLOADED SUCCESFULLY")

def CreateWidgets():
    urlLabel = tk.Label(win, text="INSTAGRAM ID: ")
    urlLabel.grid(row=0,column=0,padx=5,pady=5)
    urlLabel.config(font=("Courier",11))

    win.urlEntry = tk.Entry(win,width=30,textvariable=insta_id)
    win.urlEntry.grid(row=0,column=1,columnspan=2, pady=5)

    dwlBtn = tk.Button(win, text="Download", command=Downloader)
    dwlBtn.grid(row=0,column=5,columnspan=4,pady=5)

    win.resultLabel = tk.Label(win,textvariable=dwl_text)
    win.resultLabel.grid(row=1,column=0,columnspan=4,padx=5,pady=5)
    win.resultLabel

    win.previewLabel = tk.Label(win,text="DP Preview:")
    win.previewLabel.grid(row=3,column=0,columnspan=3, padx=5,pady=5)
    win.previewLabel.config(font=("Courier",15))

    win.dbpLabel = tk.Label(win)
    win.dbpLabel.grid(row=4)



CreateWidgets()
win.mainloop()
