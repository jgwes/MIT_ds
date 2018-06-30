from bs4 import BeautifulSoup
import urllib.request

# changes to commit

htmlDoc = urllib.request.urlopen('https://www.eecs.mit.edu/people/faculty-advisors').read().decode('utf-8')
soup = BeautifulSoup(htmlDoc, 'html.parser')

profs = []

sp = soup.find_all("span", class_="field-content card-title")
for a in sp:
    profs.append(a.get_text())

# test retrieval of profs
print(profs)

# test using Arvind
# authUrl = 'http://arxiv.org/find/eess/1/au:+Arvind/0/1/0/all/0/1'
# authData = urllib.request.urlopen(authUrl).read().decode('utf-8')
# print(authData)

# get abstract id 1712.08227 for Arvind
# absUrl = 'https://arxiv.org/abs/1712.08227'
# absDoc = urllib.request.urlopen(absUrl).read().decode('utf-8')
# soup = BeautifulSoup(absDoc, 'html.parser')

# absWords = []

# get keywords from abstract for Arvind
# sp = soup.find_all("blockquote", class_="abstract mathjax")
# for a in sp:
#    absWords.append(a.contents[2])

# print("absWords", absWords)


# Retrieve array of abstract ids for all authors
absIDs = []
authData = []
authUrl = []
baseUrl = "http://arxiv.org/find/eess/1/au:+"
urlSuffix = "/0/1/0/all/0/1"

for p in profs:
    print(p)
    authUrl = baseUrl + urllib.parse.quote(p) + urlSuffix
    print(authUrl)

# Build array of keywords from all abstract ids






