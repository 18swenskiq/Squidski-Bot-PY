from urllib.parse import quote

class GenerateWorkshopURL():
    def __init__(self):
        self.classType = "";

    def genURL(self, gameID, myType, searchTerm):
        steamString = "https://steamcommunity.com/workshop/browse/?appid=" + str(gameID) + "&searchtext=" + searchTerm + "&childpublishedfileid=0&browsesort=trend&section="
        if (myType == 'collection'): steamString += 'collections'
        elif (myType == 'item'):
            if (gameID == 730): steamString += 'mtxitems'
            else: steamString += 'readytouseitems'
        elif (myType == 'map'): steamString += 'readytouseitems'
        else: steamString += 'merchandise'
        return (steamString + "&actualsort=trend&p=1&days=-1")

    def validateSearch(self, gameID, type, searchTerm):

        print(" ")
        print("=============Workshop Search=============")
        print("Searching '" + str(gameID) + "' workshop for '" + searchTerm + "' of type: " + type)

        # Gets the ID number of the game you searched
            # Checks the type. if it is invalid, raises an error
        validTypes = ['item','items','addons','maps','merchandise','collections','map','collection','addon', 'merch', 'skin','skins']
        if (type.lower() not in validTypes):
            return "E0"
        else:
            print("User search type is " + type)
            type = self.trueType(type)
            self.classType = type;
            print("The interpreted search type is " + type)

            # Tests for invalid combos of game and type
        if (gameID == 730):
            validCSGOTypes = ['item', 'map', 'collection','merchandise']
            if (type not in validCSGOTypes): return "E1"
        elif (gameID == 620):
            validP2Types = ['item', 'map','merchandise','collection']
            if (type not in validP2Types): return "E1"
        elif (gameID == 4000):
            validGMODTypes = ['item','collection']
            if (type not in validGMODTypes): return "E1"
        elif (gameID == 550):
            validL4D2Types = ['item', 'collection']
            if (type not in validL4D2Types): return "E1"
        else: return "E5"
        print(str(gameID) + " and " + type + " are a valid combination.")

        searchTerm = searchTerm.replace(" ", "+")
        searchTerm = quote(searchTerm)
        print("New user scrubbed inputs: " + str(gameID), type, searchTerm)
        return self.genURL(gameID, type, searchTerm)

    def trueType(self, type):
        if (type.lower() == 'item' or type.lower() == 'items'): return 'item'
        elif (type.lower() == 'collection' or type.lower() == 'collections'): return 'collection'
        elif (type.lower() == 'merchandise' or type.lower() == 'merch'): return 'merchandise'
        elif (type.lower() == 'addons' or type.lower() == 'addon'): return 'item'
        elif (type.lower() == 'map' or type.lower() == 'maps'): return 'map'
        elif (type.lower() == 'skin' or type.lower() == 'skins'): return 'item'
        else: return "E3"






