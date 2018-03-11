import json
from collections import namedtuple

class Ingredient:
    """
    Class to parse and create ingredients, usually from JSON-data. Ingredients
    are stored and used in recipes

    Attributes:
    name: The name of the ingredient
    unit: units, in which the ingredient is measured in (eg. grams, litres)
    amount: number value describing the amount of said ingredient. This is
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
        return json.dumps(self.__dict__)


def ingredientFromJson(jsonIngredient):
    x = json.loads(jsonIngredient, object_hook=lambda d: namedtuple('Ingredient', d.keys())(*d.values()))
    ingredient = Ingredient(x.name,x.unit, x.amount)
    return ingredient


#THIS IS A TESTING BLOCK
#-------------------------------------------------
testIngr = Ingredient('carrot', 'grams', 500)
test2 = ingredientFromJson(testIngr.toJson())
print(testIngr)


#-------------------------------------------------