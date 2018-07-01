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

queryNames = []

# transpose names for arxiv API
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

print(queryNames)



# test using Arvind
# authUrl = 'http://arxiv.org/find/eess/1/au:+Arvind/0/1/0/all/0/1'
# authData = urllib.request.urlopen(authUrl).read().decode('utf-8')
# print(authData)

# absIds = []

# soup = BeautifulSoup(authData, 'html.parser')
# for sp in soup.find_all("a", title="Abstract"):
#    absIds.append(sp.get('href'))

# print(absIds)



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

authUrl = []
baseAuthUrl = "http://arxiv.org/find/eess/1/au:+"
authUrlSuffix = "/0/1/0/all/0/1"
authData = []

absDoc = []
baseAbsUrl = ""
absKeywords =[]

absIds = []

# for p in profs:
#     authUrl = baseAuthUrl + urllib.parse.quote(p) + authUrlSuffix
#
#     for u in authUrl:
#         print('Fetching data from {0}'.format(authUrl))
#         authData = urllib.request.urlopen(authUrl).read().decode('utf-8')
#         # parse for absId
#         print(authData)
#         soup = BeautifulSoup(authData, 'html.parser')
#         for sp in soup.find_all("a", title="Abstract"):
#             print(sp.get('href'))
#             absIds.append(sp.get('href'))
#
# print(absIds)


 #       for ad in authData:
 #           absUrl =



# Build array of keywords from all abstract ids






