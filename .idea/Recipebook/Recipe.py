from Ingredient import Ingredient

from collections import namedtuple
import json

class Recipe:
    """
    Class to create a recipe. recipe contains a list of ingredients
    as well as a short istruction.

    Attributes:
    name: The name of the recipe
    ingredients: Ingredients for the recipe
    instructions: instructions on how to cook the recipe
    """


    def __init__(self, name=None, ingredients=None, instructions=None):
        """Initializes an instance of Recipe-class
        @param name name of the recipe
        @param ingredients a list of ingredients. If one is not given,
        inits an empty list to store said ingredients
        @param instructions a simple string for instructions on how to
        cook said recipe
        """
        self.name = name
        if ingredients is None:
            self.ingredients = []
        else:
            self.ingredients = list(ingredients)
        self.instructions = instructions


    def __str__(self):
        ingrNames = [''for ingredient in self.ingredients]
        ingrStr = str(ingrNames)

        return self.name+' \n'+ingrStr+' \n Instructions: '+self.instructions


    def addIngredient(self, ingredient):
        """Adds the given ingredient-object to the recipes ingredients-list"""
        self.ingredients.append(ingredient)


    def addMultipleIngredients(self, ingredientlist):
        """Adds multiple ingredients to the recipes ingredients-list
        @param ingredientlist iterable list of ingredient-objects
        """
        self.ingredients.extend(ingredientlist)


    def toJSON(self):
        """creates a json based on the recipe, with for-space-indentation
        @returns a json-object based on the recipe
        """
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4)


    def recipeFromJson(jsonRecipe):
        """ Parses the given json, and calls to initialize a Recipe-instance
        with the values from the json-object. This solution is janky.
        """
        placeHolder = json.loads(jsonRecipe, object_hook=lambda d: namedtuple('jsonObj', d.keys())(*d.values()))
        phIngList = [] #list and a loop to transform JSON-dictionary-ingredients into actual Ingredient-type instances
        for jsonObj in placeHolder.ingredients:
            phIngList.append(Ingredient(jsonObj.name, jsonObj.unit, jsonObj.amount))
        recipe = Recipe(placeHolder.name, phIngList, placeHolder.instructions)
        return recipe


#THIS IS A TESTING BLOCK
#-------------------------------------------------
def main():
    testRecipe = Recipe(name='rice pudding', instructions='do stuff')
    carrot = Ingredient('carrot', 'unit', 1)
    testRecipe.addIngredient(carrot)
    testRecipe.addIngredient(Ingredient(name='shit', amount=500))

    testRecipe2 = Recipe.recipeFromJson(testRecipe.toJSON())
    print(testRecipe2.toJSON())
    carrot2 = Ingredient('carrot', 'unit', 5)
    testRecipe2.addIngredient(carrot2)
    print(testRecipe2.ingredients[2])

if __name__ == '__main__':
    main()

#print(testRecipe.toJSON())


#-------------------------------------------------