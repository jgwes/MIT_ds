from bs4 import BeautifulSoup
import urllib.request
from html.parser import HTMLParser


htmlDoc = urllib.request.urlopen('https://www.eecs.mit.edu/people/faculty-advisors').read().decode('utf-8')
soup = BeautifulSoup(htmlDoc, 'html.parser')

profs = []

sp = soup.find_all("span", class_="field-content card-title")
for a in sp:
    profs.append(a.get_text())

print(profs)






