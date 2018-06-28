from bs4 import BeautifulSoup
import urllib.request


htmlDoc = urllib.request.urlopen('https://www.eecs.mit.edu/people/faculty-advisors').read().decode('utf-8')
soup = BeautifulSoup(htmlDoc, 'html.parser')

profs = []

sp = soup.find_all("span", class_="field-content card-title")
for a in sp:
    profs.append(a.get_text())

print(profs)

authUrl = 'http://arxiv.org/find/eess/1/au:+Arvind/0/1/0/all/0/1'
authData = urllib.request.urlopen(authUrl).read().decode('utf-8')
print(authData)

absUrl = 'https://arxiv.org/abs/1712.08227'
absDoc = urllib.request.urlopen(absUrl).read().decode('utf-8')
soup = BeautifulSoup(absDoc, 'html.parser')

absWords = []

sp = soup.find_all("blockquote", class_="abstract mathjax")
for a in sp:
    absWords.append(a.contents[2])

print("absWords", absWords)




