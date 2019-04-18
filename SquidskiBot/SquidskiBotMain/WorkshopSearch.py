import bs4
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

    def generateWorkshopURL(game, type, searchTerm):
        # Gets the ID number of the game you searched
        # Also, why doesn't python have switch statements????
        if (lower(game) == 'csgo' or lower(game) == 'cs:go'):
            gameID = 730
        elif (lower(game) == 'portal2' or lower(game) == 'p2' or lower(game) == 'portal 2'):
            gameID = 620
        elif (lower(game) == 'gmod' or lower(game) == 'garrys mod' or lower(game) == "garry's mod"):
            gameID = 4000
        elif (lower(game) == 'l4d2' or lower(game) == 'left 4 dead 2'):
            gameID = 550
        else:
            return game + "is not a valid game"