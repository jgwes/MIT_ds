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

#url = 'http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1'
#url = 'http://export.arxiv.org/api/query?search_query=au:Arvind+AND+cat:eess'
#url = 'http://arxiv.org/find/(subject)/1/au:+(lastname)_(initial)/0/1/0/all/0/1'
url = 'http://arxiv.org/find/eess/1/au:+Arvind/0/1/0/all/0/1'
data = urllib.request.urlopen(url).read()
print(data)




