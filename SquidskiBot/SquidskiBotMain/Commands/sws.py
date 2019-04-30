from WorkshopSearch import WorkshopSearch

class sws:

    def theMain(self, userMessage):
        getSearchTerms = userMessage.split(" ")
        myGame = getSearchTerms[1]
        myType = getSearchTerms[2]
        mySearchTerm = getSearchTerms[3]

        newWSSearch = WorkshopSearch()
        messageArray = newWSSearch.getResults(myGame, myType, mySearchTerm)
        massiveCat = "1. " + messageArray["nameList"][0][2:-2] + " by " + messageArray["authorList"][0][2:-2] + ": <" + messageArray["itemList"][0] + ">"
        return (massiveCat)


