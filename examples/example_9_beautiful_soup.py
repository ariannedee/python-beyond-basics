"""
`pip install beautifulsoup4`

Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""
import re
from bs4 import BeautifulSoup

with open("data/sample.html", "r") as file:
    html_doc = file.read()

soup = BeautifulSoup(html_doc, "html.parser")


# Print the HTML document with nesting and indentation
# print(soup.prettify(formatter='html'))


# FINDING MULTIPLE ELEMENTS

a = soup.find_all("a")                             # Find all elements (returns a list)
b = soup.find_all("a", attrs={"class": "sister"})  # Filter with attributes dict
c = soup.find_all("a", class_="sister")            # Filter with keyword arguments
d = soup.find_all("a", string="Elsie")             # Filter by content
e = soup.find_all(string=re.compile(".*si.*"))     # Filter by content w/ reg ex


# FINDING A SINGLE ELEMENT

f = soup.a                                      # Get the first child element
g = soup.find("a", attrs={"id": "link1"})       # Filter with attributes dict
h = soup.find("a", id="link1")                  # Filter with keyword arguments
i = soup.find("a", string="Elsie")              # Filter by content
j = soup.find_all(string=re.compile(".*si.*"))  # Filter by content w/ reg ex


# GETTING DATA FROM AN ELEMENT
link = soup.a

k = link.string       # Get text of an element (no nested content)
l = link.text         # Get text of an element (including nested content)
m = link["href"]      # Get attribute of an element (if it exists)
n = link.get("href")  # Get attribute (if it might not exist)
o = link.contents     # Get all child elements


# NAVIGATING THE TREE
p = soup.find_all(class_="story")  # Find child elements
q = p[0].find("a")                 # Find a child element
r = q.parent                       # Get immediate parent
s = q.parents                      # Get all ancestors
u = q.next_element                 # Get next element including contents
t = q.next_sibling                 # Get next element not including contents
v = q.next_siblings                # Get all subsequent siblings

print("Use a debugger or print statement to see the value of a variable")
print(f"{a=}")
