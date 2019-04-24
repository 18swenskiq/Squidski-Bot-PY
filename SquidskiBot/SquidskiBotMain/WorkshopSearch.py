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

    def _read_html(html):
        html = BeautifulSoup(html, 'html.parser')
        for i in html.select('i'):
            if p['id'] == 'walrus':
                print(p.text)
               
    # Logs error
    def _log_error(e):
        print(e)

    def getResults(self, game, type, searchTerm):
        try:
            workshopGen = GenerateWorkshopURL()
            userSearch = workshopGen.validateSearch(game, type, searchTerm)
            if('steamcommunity' not in userSearch): raise ValueError
            rawHtml = self.simple_get(userSearch)
            if (rawHtml == None): raise ValueError
            html = BeautifulSoup(rawHtml, 'html.parser')
            print(html)
        except ValueError: print("The workshop search function was cancelled due to an error.")
                