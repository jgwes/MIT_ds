from bs4 import BeautifulSoup
import urllib.request
import pickle

class mitAbstractCollector:

    absIDs = []
    authUrls = []
    authData = []
    absDoc = []
    absUrl = []
    abstractsCollection = []
    profs = []
    queryNames = []

    baseAuthUrl = "http://arxiv.org/find/eess/1/au:+"
    #authUrlSuffix = "/0/1/0/all/0/1"
    authUrlSuffix = ""
    baseAbsUrl = "https://arxiv.org"

    abstractsCollectionFileHandler = 'keywords.pkl'

    def scrape_prof_names(self):
    #scrape professor names from MIT
        htmlDoc = urllib.request.urlopen('https://www.eecs.mit.edu/people/faculty-advisors').read().decode('utf-8')
        soup = BeautifulSoup(htmlDoc, 'html.parser')
        sp = soup.find_all("span", class_="field-content card-title")
        for a in sp:
            self.profs.append(a.get_text())

    #test
    def scrape_prof_names_test(self):

        self.profs.append("Arvind")
        self.profs.append("David Clark")

    # transpose prof names for arxiv API
    def transpose_prof_names(self):

        for p in self.profs:
            print(p)
            splitname = p.split()
            if len(splitname) < 3:
                try:
                    self.queryNames.append(splitname[1] + '_' + splitname[0][0])
                except IndexError:
                    self.queryNames.append(p.strip())

            else:
                try:
                    self.queryNames.append(splitname[2] + '_' + splitname[0][0])
                except IndexError:
                    self.queryNames.append('')

        for q in self.queryNames:
            self.authUrls.append(self.baseAuthUrl + urllib.parse.quote(q) + self.authUrlSuffix)

    # scrape abstract ids
    def scrape_abstract_ids(self):
        for u in self.authUrls:
            print('Fetching data from {0}'.format(u))
            self.authData = urllib.request.urlopen(u).read().decode('utf-8')

            soup = BeautifulSoup(self.authData, 'html.parser')

            for sp in soup.find_all("a", title="Abstract"):
                # print(sp.get('href'))
                self.absIDs.append(sp.get('href'))
                # print(absIDs)

        # scrape AbstractContent to Collection
        for a in self.absIDs:
            self.absUrl = self.baseAbsUrl + urllib.parse.quote(a)
            self.absDoc = urllib.request.urlopen(self.absUrl).read().decode('utf-8')
            soup = BeautifulSoup(self.absDoc, 'html.parser')
            sp = soup.find_all("blockquote", class_="abstract mathjax")
            for s in sp:
                self.abstractsCollection.append(s.contents[2])

        # write collection of abstracts to file
        output = open(self.abstractsCollectionFileHandler, 'wb')
        pickle.dump(self.abstractsCollection, output)
        output.close()

        #keywordsFile = open(self.abstractsCollectionFileHandler, 'rb')
        #keywords = pickle.load(keywordsFile)
        #keywordsFile.close()

    def create_abstract_file(self):
        print("scraping prof names...")
        self.scrape_prof_names_test()
        self.transpose_prof_names()
        self.scrape_abstract_ids()

    # Getter method for Abstract Collection FileName
    def get_abstract_collection_file_handler(self):
        return self.abstractsCollectionFileHandler

    # Tokenize somewhere else
    # Tokenize abstract content/keywords
    #for kw in keywords:
    #    keyword_tokens = nltk.word_tokenize(str(kw))

    # Use collections to process each abstract using a counter/dictionary


# def main():
#
#     _abstract_collector = mitAbstractCollector()
#     print("attempting to create abstract file...")
#     _abstract_collector.create_abstract_file()
#     _abstract_collection_filename = _abstract_collector.get_abstract_collection_file_handler()
#
#     _abstracts_collection_file = open(_abstract_collection_filename, 'rb')
#     _abstracts_collection = pickle.load(_abstracts_collection_file)
#     _abstracts_collection_file.close()
#
#     print("printing abstracts collection...")
#     print(_abstracts_collection[0])
#     print(_abstracts_collection[1])
#
#
# if __name__ == '__main__':
#     main()
