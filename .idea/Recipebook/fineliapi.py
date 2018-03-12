import json
from urllib.request import urlopen, Request
from urllib.parse import urlencode

class FineliAPIWatcherFactory():
    """
    A Simple class to fetch food-data through the Fineli-API.
    Currently only fetches the energy-values, but can be easily improved
    by adding more methods

    Attributes:
    url: url to the fineli-API.

    @author TET-mies
    @fixer-man Arttu Heikkilä
    @version 2.0
    """

    def __init__(self):
        self.url = 'https://fineli.fi/fineli/api/v1/foods?q={}'


    def get_calories(self, searchTerm):
        """Searches the Fineli-database with the given searchterm,
        and returns the value of the'energyKcal'-key of the first
        ingredient found
        """
        try:
            fineliData = self.fetchFromAPI(searchTerm)
            foodJson = json.loads(fineliData)               #Init a json-object based on the data from the response
            firstResultCalories = foodJson[0]['energyKcal'] #Gets the value of 'energyKcal' from the first in the list
            return firstResultCalories
        except:
            print('No search results for the ingredient: %s' %searchTerm)


    def fetchFromAPI(self, searchTerm):
        """formats the full URL from with the search term
        and makes the API-call. If the searchTerm contains
        unicode, it will be encoded to proper format"""
        fullUrl = '{}?{}'.format(self.url, urlencode({'searchTerm': searchTerm})) #This line encodes unicode characters to url/percent-encoding
        req = Request(fullUrl, headers={'User-Agent': 'Mozilla/5.0'})
        return urlopen(req).read()


#Testing block for the class.
#Use this to test the functionality.
#-----------------------------------------------------
if __name__ == '__main__':
    factory = FineliAPIWatcherFactory()
    cals = factory.get_calories('voi')
    print(cals)
#-----------------------------------------------------