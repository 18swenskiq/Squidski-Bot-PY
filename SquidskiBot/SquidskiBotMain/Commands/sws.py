from WorkshopSearch import WorkshopSearch

class sws:
    def theMain(self, game, myType, searchTerm):
        newWSSearch = WorkshopSearch()
        messageArray = newWSSearch.getResults(game, myType, searchTerm)
        return ("Result 1: <" + messageArray[0] + ">\nResult 2: <" + messageArray[1] + ">\nResult 3: <" + messageArray[2] + ">\nResult 4: <" + messageArray[3] + ">\nResult 5: <" + messageArray[4] + ">")


