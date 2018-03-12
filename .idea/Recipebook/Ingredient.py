import json

class Ingredient:
    """
    Class to parse and create ingredients, usually from JSON-data. Ingredients
    are stored and used in recipes

    Attributes:
        name: The name of the ingredient
        unit: units, in which the ingredient is measured in (eg. grams, litres)
        amount: number value describing the amount of units
    """


    def __init__(self, name=None, unit=None, amount=None):
        """initializes instance of the ingredient class with
        each attribute mapped with given param
        """
        self.name = name
        self.amount = amount
        self.unit = unit


    def __str__(self):
        return self.name+': '+str(self.amount)+' '+self.unit


    def toJson(self):
        """Returns the object in json-format"""
        return json.dumps(self.__dict__)


    def ingredientFromJson(jsonData):
       # x = json.loads(jsonIngredient, object_hook=lambda d: namedtuple('Ingredient', d.keys())(*d.values()))
        ingredient = Ingredient(jsonData['name'],jsonData['unit'], jsonData['amount'])
        return ingredient


#THIS IS A TESTING BLOCK
#-------------------------------------------------



#-------------------------------------------------