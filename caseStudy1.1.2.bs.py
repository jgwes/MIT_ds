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
authUrlSuffix = "/0/1/0/all/0/1"

authUrlSuffix = ""
authData = []
absDoc = []
baseAbsUrl = "https://arxiv.org"
absUrl = []
keyWordsCollection = []
profs = []
queryNames = []


#scrape professor names from MIT
#htmlDoc = urllib.request.urlopen('https://www.eecs.mit.edu/people/faculty-advisors').read().decode('utf-8')
#soup = BeautifulSoup(htmlDoc, 'html.parser')
#sp = soup.find_all("span", class_="field-content card-title")
#for a in sp:
#    profs.append(a.get_text())

profs.append("Arvind")
profs.append("David Clark")

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
        keyWordsCollection.append(k.contents)

#print(keyWordsCollection[0])
#print(keyWordsCollection[1])

# pickle
output = open('keywords.pkl', 'wb')
pickle.dump(keyWordsCollection, output)
output.close()

keywordsFile = open('keywords.pkl', 'rb')
keywords = pickle.load(keywordsFile)
keywordsFile.close()

# Tokenize abstract content/keywords
#for kw in keyWordsCollection:
#    keyword_tokens = nltk.word_tokenize(kw[0])
#print(keyword_tokens)

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

# class sviLda():
#
#     def __init__(self, vocab, K, D, alpha, eta, tau, kappa, docs, iterations):
#         self._vocab = vocab
#         self._V = len(vocab)
#         self._K = K
#         self._D = D
#         self._alpha = alpha
#         self._eta = eta
#         self._tau = tau
#         self._kappa = kappa
#         self._lambda = 1* numpy.random.gamma(100., 1./100., (self._K, self._V))
#         self._Elogbeta = sviLda.dirichlet_expectation(self._lambda)
#         self._expElogbeta = numpy.exp(self._Elogbeta)
#         self._docs = docs
#         self.ct = 0
#         self._iterations = iterations
#
#     def dirichlet_expectation(alpha):
#         # calculate the expectation for a beta distribution given parameter alpha
#         # from onlinedavb.py by Matthew Hoffman
#         if(len(alpha.shape) == 1):
#             return psi(alpha) - psi(numpy.sum(alpha))
#         return psi(alpha) - psi(numpy.sum(alpha,1))[:,numpy.newaxis]
#
#     def updateLocal(self, doc):
#         # take parsed document, update local variables
#         (words, counts) = doc
#         newdoc = []
#         N_d = sum(counts)
#         phi_d = numpy.zeros((self._K, N_d))
#         gamma_d = numpy.random.gamma(100.,1./100.,(self._K))
#         Elogtheta_d = sviLda.dirichlet_expectation(gamma_d)
#         expElogtheta_d = numpy.exp(Elogtheta_d)
#         for i,item in enumerate(counts)
#             for j in range(item):
#                 newdoc.append(words[i])
#         assert len(newdoc) == N_d, "error"
#
#         for i in range(self._iterations):
#             for m, word in enumerate(newdoc):
#                 phi_d[:,m] = numpy.multiply(expElogtheta_d, self._expElogbeta[:,word]) + 1e-100
#                 phi_d[:,m] = phi_d[:,m]/numpy.sum(phi_d[:,m])
#
#             gamma_new = self._alpha + numpy.sum(phi_d,axis=1)
#             meanchange = numpy.mean(abs(gamma_d -gamma_new))
#             if(meanchange < meanthresh):
#                 break
#
#             gamma_d = gamma_new
#             Elogtheta_d = dirichlet_expectation(gamma_d)
#             expElogtheta_d = numpy.exp(Elogtheta_d)
#
#         newdoc = numpy.asarray(newdoc)
#         return phi_d, newdoc, gamma_d
#
#     def updateGlobal(self, local_param, doc):
#         lambda_d = numpy.zeros((self._K, self._V))
#         for k in range(self._K):
#             phi_dk = numpy.zeros(self._V)
#             for m, word in enumerate(doc):
#                 phi_dk[word] += phi_d[k][m]
#             lambda_d[k] = self._eta + self._D * phi_dk
#         rho = (self.ct + self._tau)**(-self._kappa)
#         self._lambda = (1-rho)*self._lambda+rho*lambda_d
#         self._Elogbeta = dirichlet_expectation(self._lambda)
#         self._expElogbeta = numpy.exp(self._Elogbeta)
#
#     def runSVI(self):
#         for i in range(self._iterations):
#             randint = random.radnint(0,self._D-1)
#             print "ITERATION", i, " running document number ",
#             randint doc = parseDocument(self._docs[randint],self._vocab) phi_doc,
#             newdoc,
#             gamma_d = self.updateLocal(doc) self.updateGlobal(phi_doc, newdoc)
#             self.ct += 1
#
#     def parseDocument(doc, vocab):
#         wordslist = list()
#         countslist = list()
#         doc = doc.lower()
#         tokens = wordpunct_tokenize(doc)
#         for word in tokens:
#             if word in vocab: wordtk = vocab[word]
#                 if wordtk not in dictionary:
#                     dictionary[wordtk] = 1
#                 else:
#                     dictionary[wordtk] += 1
#                 wordslist.append(dictionary.keys())
#                 countslist.append(dictionary.values())
#             return (wordslist[0], countslist[0])





















