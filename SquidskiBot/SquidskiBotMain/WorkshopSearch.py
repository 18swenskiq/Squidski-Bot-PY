import bs4
import discord
import re
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

from GenerateWorkshopURL import GenerateWorkshopURL

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
        try:
            workshopGen = GenerateWorkshopURL()
            userSearch = workshopGen.validateSearch(game, myType, searchTerm)
            print("User Search URL SHOULD be: " + userSearch)
            if('steamcommunity' not in userSearch): raise ValueError
            rawHtml = self.simple_get(userSearch)
            if (rawHtml == None): raise ValueError
            html = BeautifulSoup(rawHtml, 'html.parser')
            tempWorkshopItemList = []
            bigNumber = 100000000

            while(bigNumber < 3000000000):
                myNewHTML = html.find("a", {"data-publishedfileid" : str(bigNumber)})
                print(myNewHTML)
                bigNumber += 1
            #html = str(html).split("\n")
            #for line in html:
            #    print(html)
            #    if ('<div id="sharedfile_"' in line):
            #        print(line)
            #        myIndex = 21
            #        myNewString = ""
            #        while (not line[myIndex] == '"'):
            #            myNewString += line[myIndex]
            #        tempWorkshopItemList += myNewString
            #        if (iters == 5): break
            #        iters += 1

            workshopItemList = []
            for item in tempWorkshopItemList:
                workshopItemList += "https://steamcommunity.com/sharedfiles/filedetails/?id=" + item

            return(workshopItemList)
        except ValueError: print("The workshop search function was cancelled due to an error.")