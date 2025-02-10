import requests
import base64
import urllib
import ctypes
import os
import sys
import datetime
import time
import random

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
    time.sleep(5)
    IMAGE = random.randint(1,100)
    PAGE = random.randint(1,50)
    URL = f"https://e621.net/posts.json?page={PAGE}&limit=100&tags=16%3A9+-animated+order%3Ascore"
    REQUEST = requests.get(URL, headers=HEADER).json()
    BGURL = str(REQUEST['posts'][IMAGE]['file']['url'])
    urllib.request.urlretrieve(BGURL, "image.jpg")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(os.path.dirname(sys.argv[0])) + "\image.jpg", 0)