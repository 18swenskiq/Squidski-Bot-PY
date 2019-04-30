from urllib.parse import quote

class GenerateWorkshopURL():
    def genURL(self, gameID, myType, searchTerm):
        steamString = "https://steamcommunity.com/workshop/browse/?appid=" + str(gameID) + "&searchtext=" + searchTerm + "&childpublishedfileid=0&browsesort=trend&section="
        if (myType == 'collection'): steamString += 'collections'
        elif (myType == 'item'):
            if (gameID == 730): steamString += 'mtxitems'
            else: steamString += 'readytouseitems'
        elif (myType == 'map'): steamString += 'readytouseitems'
        else: steamString += 'merchandise'
        return (steamString + "&actualsort=trend&p=1&days=-1")

    def validateSearch(self, game, type, searchTerm):
        errorMessage = "Nothing was assigned"

        print(" ")
        print("=============Workshop Search=============")
        print("Searching '" + game + "' workshop for '" + searchTerm + "' of type: " + type)

        # Gets the ID number of the game you searched
        try:
            if (game.lower() == 'csgo' or game.lower() == 'cs:go'): gameID = 730
            elif (game.lower() == 'portal2' or game.lower() == 'p2' or game.lower() == 'portal 2'): gameID = 620
            elif (game.lower() == 'gmod' or game.lower() == 'garrys mod' or game.lower() == "garry's mod"): gameID = 4000
            elif (game.lower() == 'l4d2' or game.lower() == 'left 4 dead 2'): gameID = 550
            else:
                errorMessage = game + " is not a valid game"
                print(game + " was tried as a valid game (its not).")
                raise ValueError(f"The game '{game}' is invalid.")
            print("GameID interepreted as " + str(gameID) + " from user input of: " + game)
            
            # Checks the type. if it is invalid, raises an error
            validTypes = ['item','items','addons','maps','merchandise','collections','map','collection','addon', 'merch', 'skin','skins']
            if (type.lower() not in validTypes):
                errorMessage = type + " is not a valid type"
                print(type + " was tried as a valid type (its not).")
                raise ValueError(f"The type '{type}' is invalid.")
            else:
                print("User search type is " + type)
                type = self.trueType(type)
                print("The interpreted search type is " + type)

            # Tests for invalid combos of game and type
            if (gameID == 730):
                validCSGOTypes = ['item', 'map', 'collection','merchandise']
                if (type not in validCSGOTypes):
                    errorMessage = type + " is not a valid type for CS:GO"
                    raise ValueError
            elif (gameID == 620):
                validP2Types = ['item', 'map','merchandise','collection']
                if (type not in validP2Types):
                    errorMessage = type + " is not a valid type for Portal2"
                    raise ValueError
            elif (gameID == 4000):
                validGMODTypes = ['item','collection']
                if (type not in validGMODTypes):
                    errorMessage = type + " is not a valid type for Garry's Mod"
                    raise ValueError
            elif (gameID == 550):
                validL4D2Types = ['item', 'collection']
                if (type not in validL4D2Types):
                    errorMessage = type + " is not a valid type for L4D2"
                    raise ValueError
            else:
                errorMessage = "An unknown error occurred. Attempted types were " + type + " and " + game
                raise ValueError
            print(str(gameID) + " and " + type + " are a valid combination.")

            # Scrubs searchTerm
            searchTerm = searchTerm.replace(" ", "+")
            searchTerm = quote(searchTerm)
            print("New user scrubbed inputs: " + str(gameID), type, searchTerm)
            return self.genURL(gameID, type, searchTerm)
        except (ValueError): return "Operation Failed"

    def trueType(self, type):
        if (type.lower() == 'item' or type.lower() == 'items'): return 'item'
        elif (type.lower() == 'collection' or type.lower() == 'collections'): return 'collection'
        elif (type.lower() == 'merchandise' or type.lower() == 'merch'): return 'merchandise'
        elif (type.lower() == 'addons' or type.lower() == 'addon'): return 'item'
        elif (type.lower() == 'map' or type.lower() == 'maps'): return 'map'
        elif (type.lower() == 'skin' or type.lower() == 'skins'): return 'item'
        else: return 'item'





