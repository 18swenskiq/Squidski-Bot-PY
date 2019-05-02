from urllib.parse import quote

class GenerateWorkshopURL():
    def genURL(self, gameID, myType, searchTerm):
        try:
            steamString = "https://steamcommunity.com/workshop/browse/?appid=" + str(gameID) + "&searchtext=" + searchTerm + "&childpublishedfileid=0&browsesort=trend&section="
            if (myType == 'collection'): steamString += 'collections'
            elif (myType == 'item'):
                if (gameID == 730): steamString += 'mtxitems'
                else: steamString += 'readytouseitems'
            elif (myType == 'map'): steamString += 'readytouseitems'
            else: steamString += 'merchandise'
            return (steamString + "&actualsort=trend&p=1&days=-1")
        except: return 4

    def validateSearch(self, gameID, type, searchTerm):

        print(" ")
        print("=============Workshop Search=============")
        print("Searching '" + str(gameID) + "' workshop for '" + searchTerm + "' of type: " + type)

        # Gets the ID number of the game you searched
        try:
            # Checks the type. if it is invalid, raises an error
            validTypes = ['item','items','addons','maps','merchandise','collections','map','collection','addon', 'merch', 'skin','skins']
            if (type.lower() not in validTypes):
                errorMessage = type + " is not a valid type"
                print(type + " was tried as a valid type (its not).")
                raise ValueError
            else:
                print("User search type is " + type)
                type = self.trueType(type)
                print("The interpreted search type is " + type)
        except: return 0

        try:
            # Tests for invalid combos of game and type
            if (gameID == 730):
                validCSGOTypes = ['item', 'map', 'collection','merchandise']
                if (type not in validCSGOTypes): raise ValueError
            elif (gameID == 620):
                validP2Types = ['item', 'map','merchandise','collection']
                if (type not in validP2Types): raise ValueError
            elif (gameID == 4000):
                validGMODTypes = ['item','collection']
                if (type not in validGMODTypes): raise ValueError
            elif (gameID == 550):
                validL4D2Types = ['item', 'collection']
                if (type not in validL4D2Types): raise ValueError
            else: raise ValueError
            print(str(gameID) + " and " + type + " are a valid combination.")
        except: return 1

        try:
            # Scrubs searchTerm
            searchTerm = searchTerm.replace(" ", "+")
            searchTerm = quote(searchTerm)
            print("New user scrubbed inputs: " + str(gameID), type, searchTerm)
            newURL = self.genURL(gameID, type, searchTerm)
            try:
                if (isinstance(newURL, int)): raise ValueError
            except: return 4
            return self.genURL(gameID, type, searchTerm)
        except: return 2

    def trueType(self, type):
        try:
            if (type.lower() == 'item' or type.lower() == 'items'): return 'item'
            elif (type.lower() == 'collection' or type.lower() == 'collections'): return 'collection'
            elif (type.lower() == 'merchandise' or type.lower() == 'merch'): return 'merchandise'
            elif (type.lower() == 'addons' or type.lower() == 'addon'): return 'item'
            elif (type.lower() == 'map' or type.lower() == 'maps'): return 'map'
            elif (type.lower() == 'skin' or type.lower() == 'skins'): return 'item'
            else: raise ValueError
        except: return 3






