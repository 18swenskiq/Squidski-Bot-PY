from WorkshopSearch import WorkshopSearch

class sws:

    def theMain(self, userMessage):
        getSearchTerms = userMessage.split(" ")
        myGame = getSearchTerms[1]
        myType = getSearchTerms[2]
        mySearchTerm = getSearchTerms[3]
        massiveCat = ""
        iters = 1

        newWSSearch = WorkshopSearch()
        messageArray = newWSSearch.getResults(myGame, myType, mySearchTerm)
        for item in messageArray["itemList"]:
            massiveCat += str(iters) + ". " + (messageArray["nameList"][iters - 1][2:-2]).translate( + " by " + (messageArray["authorList"][iters - 1][2:-2]) + ": <" + messageArray["itemList"][iters - 1] + ">\n\n"
            iters += 1
        return (massiveCat)


