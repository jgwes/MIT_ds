from bs4 import BeautifulSoup
import urllib.request

absIDs = []
authUrls = []
baseAuthUrl = "http://arxiv.org/find/eess/1/au:+"
#authUrlSuffix = "/0/1/0/all/0/1"
authUrlSuffix = ""
authData = []
absDoc = []
baseAbsUrl = "https://arxiv.org"
absUrl = []
keyWords = []
profs = []
queryNames = []


# scrape professor names from MIT
# htmlDoc = urllib.request.urlopen('https://www.eecs.mit.edu/people/faculty-advisors').read().decode('utf-8')
# soup = BeautifulSoup(htmlDoc, 'html.parser')
# sp = soup.find_all("span", class_="field-content card-title")
# for a in sp:
#    profs.append(a.get_text())

profs.append("Arvind")

# transpose prof names for arxiv API
for p in profs:
    print(p)
    splitName = p.split()
    if len(splitName) < 3:
        try:
            queryNames.append(splitName[1] + '_' + splitName[0][0])
        except IndexError:
            queryNames.append(p.strip())
    else:
        try:
            queryNames.append(splitName[2] + '_' + splitName[0][0])
        except IndexError:
            queryNames.append('')

for q in queryNames:
    authUrls.append(baseAuthUrl + urllib.parse.quote(q) + authUrlSuffix)

# scrape abstract ids
for u in authUrls:
     print('Fetching data from {0}'.format(u))
     authData = urllib.request.urlopen(u).read().decode('utf-8')

     soup = BeautifulSoup(authData, 'html.parser')

     for sp in soup.find_all("a", title="Abstract"):
        # print(sp.get('href'))
        absIDs.append(sp.get('href'))
        # print(absIDs)

# scrape keywords
for a in absIDs:
    absUrl = baseAbsUrl + urllib.parse.quote(a)
    absDoc = urllib.request.urlopen(absUrl).read().decode('utf-8')
    soup = BeautifulSoup(absDoc, 'html.parser')
    sp = soup.find_all("blockquote", class_="abstract mathjax")
    for k in sp:
        keyWords.append(a.contents[2])