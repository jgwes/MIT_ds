from bs4 import BeautifulSoup
import urllib.request
import pickle
from io import StringIO
import nltk
import collections
import numpy
from scipy.special import gammaln, psi

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
        keyWords.append(k.contents[2])

# pickle
output = open('keywords.pkl', 'wb')
pickle.dump(keyWords, output)
output.close()

keywordsFile = open('keywords.pkl', 'rb')
keywords = pickle.load(keywordsFile)
keywordsFile.close()

# Tokenize abstract content/keywords
keyword_tokens = nltk.word_tokenize(keywords[0])
print(keyword_tokens)

# Use collections to process each abstract using a counter/dictionary


# Implement Latent Dirichlet Allocation (LDA) to discover topics
#
#     lambda = posterior distribution of topics for each word
#     vocab = vocabulary in the documents
#     K = number of topics
#     D = total number of documents
#     alpha = parameter for per-document topic distribution
#     eta = parameter for per-topic vocab distribution
#     tau = delay to weigh down early iterations
#     kappa = forgetting rate, larger the value, the slower old info is forgotten
#     max:iterations =  maximum iterations the updates should go on for. Check
#                     if the delta in two consecutive values of lambda
#                     is smaller than a certain value, the algorithm has converged.
#                     Setting this value too small, the updates may run forever

class sviLda():

    def __init__(self, vocab, K, D, alpha, eta, tau, kappa, docs, iterations):
        self._vocab = vocab
        self._V = len(vocab)
        self._K = K
        self._D = D
        self._alpha = alpha
        self._eta = eta
        self._tau = tau
        self._kappa = kappa
        self._lambda = 1* numpy.random.gamma(100., 1./100., (self._K, self._V))
        self._Elogbeta = dirichlet_expectation(self._lambda)
        self._expElogbeta = numpy.exp(self._Elogbeta)
        self._docs = docs
        self.ct = 0
        self._iterations = iterations

    def dirichlet_expecation(alpha):
        if(len(alpha.shape) == 1):
            return psi(alpha) - psi(numpy.sum(alpha))
        return psi(alpha) - psi(numpy.sum(alpha,1))[:,numpy.newaxis]






















