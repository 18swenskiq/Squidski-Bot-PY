from ErrorStrings import ErrorStrings
from WorkshopSearch import WorkshopSearch

class sws:

    def theMain(self, userMessage):
        newWSSearch = WorkshopSearch()
        myErrors = ErrorStrings()

        getSearchTerms = userMessage.split(" ")
        if len(getSearchTerms) < 4:
            return myErrors.E8()
        myGame = getSearchTerms[1]
        myType = getSearchTerms[2]
        mySearchTerm = getSearchTerms[3]
        massiveCat = ""
        iters = 1

        messageArray = newWSSearch.getResults(myGame, myType, mySearchTerm)
        if (isinstance(messageArray, str)):
            if (messageArray.startswith("E")):
                print(messageArray)
                return (eval("myErrors." + messageArray + "()"))
            else:
                return "An unknown error occured"
        print(messageArray)
        for item in messageArray["itemList"]:
            massiveCat += str(iters) + ". " + ((messageArray["nameList"][iters - 1][2:-2]).replace("', '", ' ')).replace("\", '",' ') + " by '" + ((messageArray["authorList"][iters - 1][2:-2]).replace("', '", ' ')).replace("\", '",' ') + "': <" + messageArray["itemList"][iters - 1] + ">\n\n"
            iters += 1
        return (massiveCat)


