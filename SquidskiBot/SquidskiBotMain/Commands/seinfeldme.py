import random

class seinfeldme():
    quoteList = []

    # Reads SeinfeldQuotes.txt and puts all lines into a list
    def __init__(self):
        myFile = open("SeinfeldQuotes.txt", "r")
        self.quoteList = (myFile.read()).split("\n")
        myFile.close();

    # Pulls and sends a random quote
    def getQuote(self):
        return random.choice(self.quoteList)


