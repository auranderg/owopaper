import urllib.request
import requests
import base64
import json
import urllib
import ctypes
import os
import sys

URL = "https://e621.net/posts.json?limit=1&tags=16%3A9+-animated+order%3Ascore"

USER = "ZinnoSinno"
API = "TBaR8JBdkwacWaxEVzugDGkC"

AUTH = base64.b64encode(f"{USER}:{API}".encode())

HEADER = {
    "Authorization": f"Basic {AUTH.decode()}",
    "User-Agent": "owopaper by zinnosinno on e621"
}

r = requests.get(URL, headers=HEADER).json()

with open("json.json", "w") as file:
    json.dump(r, file, indent=4)

print(r['posts'][0]['file']['url'])

BGURL = str(r['posts'][0]['file']['url'])

urllib.request.urlretrieve(BGURL, "image.jpg")

ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(os.path.dirname(sys.argv[0])) + "\image.jpg", 0)