""" Scraping """

from urllib.request import urlopen

def grab_html():
    url = input("Pega aquí tu url.")
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
