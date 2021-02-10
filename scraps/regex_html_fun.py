""" Scraping """
from urllib.request import urlopen
import re

def grab_html():
    url = input("Pega aquí tu url.")
    page = urlopen(url)
    html_bytes = page.read()
    global html 
    html = html_bytes.decode("utf-8")


grab_html()

pattern = "<title.*?>.*?</title.*?>"
matches = re.search(pattern, html, re.IGNORECASE)
title = matches.group()
title = re.sub("<.*?>", "", title)
print(title)

