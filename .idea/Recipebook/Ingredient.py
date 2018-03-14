import json

class Ingredient:
    """
    Class to parse and create ingredients, usually from JSON-data.
    Attributes:
        name: The name of the ingredient
        unit: units, in which the ingredient is measured in (eg. grams, litres)
        amount: number value describing the amount of units
    """


    def __init__(self, name=None, unit=None, amount=None):
        self.name = name
        self.amount = amount
        self.unit = unit


    def __str__(self):
        return self.name+': '+str(self.amount)+' '+self.unit


    def toJson(self):
        """@returns the object in json-format"""
        return json.dumps(self.__dict__)


    def ingredientFromJson(jsonData):
        """Parses the given json and initializes Ingredient-instance
        @returns ingredient-instance"""
        ingredient = Ingredient(jsonData['name'],jsonData['unit'], jsonData['amount']) #initializes Ingredient with values from json
        return ingredient