from ErrorStrings import ErrorStrings
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
        myErrors = ErrorStrings()

        #TODO: FIX ERROR HANDLING

        messageArray = newWSSearch.getResults(myGame, myType, mySearchTerm)
        if (isinstance(messageArray, ValueError)): return "test error"
        print(messageArray)
        for item in messageArray["itemList"]:
            massiveCat += str(iters) + ". " + (messageArray["nameList"][iters - 1][2:-2]).replace("', '", ' ') + " by '" + (messageArray["authorList"][iters - 1][2:-2]).replace("', '", ' ') + "': <" + messageArray["itemList"][iters - 1] + ">\n\n"
            iters += 1
        return (massiveCat)


