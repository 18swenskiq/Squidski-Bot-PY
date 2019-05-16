import random

class seinfeldme():
    quoteList = []

    def __init__(self):
        myFile = open("SeinfeldQuotes.txt", "r")
        self.quoteList = (myFile.read()).split("\n")
        myFile.close();

    def getQuote(self):
        return random.choice(self.quoteList)


