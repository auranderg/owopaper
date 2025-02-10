import requests
import base64
import urllib
import ctypes
import os
import sys
import datetime
import time
import random
import pystray
import tkinter
from tkinter import *
from tkinter import ttk

ROOT = Tk()
FRAME = ttk.Frame(ROOT, padding = 10)
FRAME.grid()
ttk.Label(FRAME, text="owopaper by Auran").grid(column = 0, row = 0)
TAGS = tkinter.StringVar()
TEXT = ttk.Entry(ROOT, textvariable = TAGS)
TEXT.grid(column = 0, row = 1)
TEXT.insert(0, "16:9 -animated order:score ")

ttk.Button(FRAME, text="Run", command=ROOT.destroy).grid(column = 0, row = 2)
ROOT.mainloop()

# will soon configure username, api key

USER = "ZinnoSinno"
API = "TBaR8JBdkwacWaxEVzugDGkC"
AUTH = base64.b64encode(f"{USER}:{API}".encode())
HEADER = {
    "Authorization": f"Basic {AUTH.decode()}",
    "User-Agent": "owopaper by zinnosinno on e621"
}

# unused function to repeat at a given time
'''
def AT(HOUR, MINUTE):
    while True:
        NOW = datetime.datetime.now()
        if NOW.hour == HOUR and NOW.minute == MINUTE:
            break
        time.sleep(1)
'''

while True:
    PAGE = random.randint(1,50)
    URL = f"https://e621.net/posts.json?page={PAGE}&limit=100&tags={TAGS.get()}"
    REQUEST = requests.get(URL, headers=HEADER).json()
    COUNT = len(REQUEST['posts'])
    IMAGE = random.randint(1,COUNT)
    print(f"Limit: 100")
    print(f"Page number: {PAGE}")
    print(f"Post count: {COUNT}")
    print(f"Image index: {IMAGE}")
    print(f"Tags: {TAGS.get()}")

    BGURL = str(REQUEST['posts'][IMAGE]['file']['url'])
    urllib.request.urlretrieve(BGURL, "image.jpg")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(os.path.dirname(sys.argv[0])) + "\image.jpg", 0)

    time.sleep(5)