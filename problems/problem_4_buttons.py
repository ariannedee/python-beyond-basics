"""
Print the text of all buttons on the Google homepage
"""
from bs4 import BeautifulSoup

with open("data/google.html", "r") as file:
    html_doc = file.read()

print(html_doc)
