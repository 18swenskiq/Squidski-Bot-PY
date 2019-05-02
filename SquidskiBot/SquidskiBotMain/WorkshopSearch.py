import bs4
import discord
import re
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

from GenerateWorkshopURL import GenerateWorkshopURL
from ErrorStrings import ErrorStrings

class WorkshopSearch:
    def __init__(self):
        self.data = []

    def simple_get(self, url):
        try:
            with closing(get(url, stream=True)) as resp:
                if self.is_good_response(resp):
                 return resp.content
                else:
                 return None

        except RequestException as e:
          log_error('Error during requests to {0} : {1}'.format(url, str(e)))
          return None

    def is_good_response(self, resp):
        content_type = resp.headers['Content-Type'].lower()
        return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)
               
    # Logs error
    def _log_error(e):
        print(e)

    def getResults(self, game, myType, searchTerm):
        if (game.lower() == 'csgo' or game.lower() == 'cs:go'): gameID = 730
        elif (game.lower() == 'portal2' or game.lower() == 'p2' or game.lower() == 'portal 2'): gameID = 620
        elif (game.lower() == 'gmod' or game.lower() == 'garrys mod' or game.lower() == "garry's mod"): gameID = 4000
        elif (game.lower() == 'l4d2' or game.lower() == 'left 4 dead 2'): gameID = 550
        else:
            print(game + " was tried as a valid game (its not).")
            return "E5"
        print("GameID interepreted as " + str(gameID) + " from user input of: " + game)

        workshopGen = GenerateWorkshopURL()
        myErrors = ErrorStrings()
        userSearch = workshopGen.validateSearch(gameID, myType, searchTerm)
        if (isinstance(userSearch, str)):
            print(userSearch)
            if (userSearch.startswith("E")):
                return userSearch[:1]
        print("User Search URL SHOULD be: " + userSearch)
        if('steamcommunity' not in userSearch): return "E6"
        print("Searching the Workshop now...")
        rawHtml = self.simple_get(userSearch)
        if (rawHtml == None): return "E7"

            # Parses the HTML file
        html = BeautifulSoup(rawHtml, 'html.parser').prettify().split("\n")
        print("Workshop HTML page successfully retrieved and parsed.")

            # Now we're looping through the whole HTML to find the first 5 maps
        place = 0
        workshopItemList = []
        itemNameList = []
        workshopAuthorName = []

        while (place < len(html)):

            if ("data-publishedfileid" in html[place]):
                print("Getting Workshop Item URL...")
                newHtml = str((html[place].split(" "))[12])
                sliceInt = -18 - len(searchTerm)
                workshopItemList.append(str(newHtml[6:sliceInt]))

            if ("workshopItemTitle" in html[place]):
                print("Getting Workshop Item Title #...")
                newTitle = str((html[place + 1].split(" "))[11:])
                itemNameList.append(str(newTitle))

            if ("workshopItemAuthorName" in html[place]):
                print("Getting Workshop Item Primary Author...")
                newAuthor = str((html[place + 3].split(" "))[11:])
                workshopAuthorName.append(str(newAuthor))

            place += 1
            if (len(workshopAuthorName) > 4): break

        returnObj = {
            "itemList": workshopItemList,
            "nameList": itemNameList,
            "authorList": workshopAuthorName
            }
        return(returnObj)