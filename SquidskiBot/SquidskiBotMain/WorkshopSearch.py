import bs4
import discord
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

class WorkshopSearch:
    def __init__(self):
        self.data = []

    def _simple_get(url):
        try:
            with closing(get(url, stream=True)) as resp:
                if is_good_response(resp):
                 return resp.content
                else:
                 return None

        except RequestException as e:
          log_error('Error during requests to {0} : {1}'.format(url, str(e)))
          return None

    def _is_good_response(resp):
        content_type = resp.headers['Content-Type'].lower()
        return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)

    def _read_html(html):
        html = BeautifulSoup(html, 'html.parser')
        for i in html.select('i'):
            if p['id'] == 'walrus':
                print(p.text)
               
    # Logs error
    def _log_error(e):
        print(e)

    def _true_type(type):
        if (lower(type) == 'item' or lower(type) == 'items'):
            return 'item'
        elif (lower(type) == 'collection' or lower(type) == 'collections'):
            return 'collection'
        elif (lower(type) == 'merchandise' or lower(type) == 'merch'):
            return 'merchandise'
        elif (lower(type) == 'addons' or lower(type) == 'addon'):
           return 'addon'
        elif (lower(type) == 'map' or lower(type) == 'maps'):
           return 'map'
        else:
           return 'item' # this should never happen

    async def generateWorkshopURL(game, type, searchTerm):
        # Gets the ID number of the game you searched
        try:
            # if the game is invalid, an error is raised
            try:
                if (lower(game) == 'csgo' or lower(game) == 'cs:go'):
                    gameID = 730
                elif (lower(game) == 'portal2' or lower(game) == 'p2' or lower(game) == 'portal 2'):
                    gameID = 620
                elif (lower(game) == 'gmod' or lower(game) == 'garrys mod' or lower(game) == "garry's mod"):
                    gameID = 4000
                elif (lower(game) == 'l4d2' or lower(game) == 'left 4 dead 2'):
                    gameID = 550
                else:
                    raise NameError
            except:
                errorMessage = game + " is not a valid game"
                print(game + " was tried as a valid game (its not).")
                raise NameError
            
            # Checks the type. if it is invalid, raises an error
            try:
                validTypes = ['item','items','addons','maps','merchandise','collections','map','collection','addon', 'merch']
                if (lower(type) not in validTypes):
                    raise NameError
                else:
                    type = true_type(type)

            except:
                errorMessage = type + " is not a valid type"
                print(type + " was tried as a valid type (its not).")
                raise NameError

            # Tests for invalid combos of game and type
            try:
                validCSGOTypes = ['item']
        except:
            await message.channel.send('The operation failed. ' + errorMessage)
