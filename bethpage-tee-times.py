import requests as re
import twilio, flask
from bs4 import BeautifulSoup as bs
import os
print(os.path.expanduser('~'))


base_url = "https://foreupsoftware.com/index.php/booking/19765/2431#/teetimes"
dir = f"{os.path.expanduser('~')}\\.keys\\"
print(dir)
with open(f'{dir}bethpage-username') as f:
    us = f.readline()

with open(f'{dir}bethpage') as f:
    ps = f.readline()


