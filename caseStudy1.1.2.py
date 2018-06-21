import urllib.request
from html.parser import HTMLParser

class htmlParser(HTMLParser):

    #spamTag = '<span class="field-content card-title">'
    lsStartTags = list()
    d = list()

    def handle_starttag(self, tag, attrs):
        if (tag == 'span'):
            for attr in attrs:
                if 'card-title' in attr[1]:
                    d = d.append(attr[1])
                    #print(attr[1])
                    #self.handle_data(d)


    def handle_data(self, data):
        print(data)

parser = htmlParser()

htmlDoc = urllib.request.urlopen('https://www.eecs.mit.edu/people/faculty-advisors').read().decode('utf-8')

parser.feed(htmlDoc)
#Sprint(parser.lsStartTags)



