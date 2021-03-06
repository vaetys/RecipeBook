from Ingredient import Ingredient
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
        """Initializes an instance of Recipe-class"""
        self.name = name
        if ingredients is None: #If a ready list of ingredients is not given, creates an empty list
            self.ingredients = []
        else:
            self.ingredients = ingredients
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


    def toJson(self):
        """creates a json based on the recipe, with for-space-indentation
        @returns a json-object based on the recipe
        """
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4)


    def recipeFromJson(jsonRecipe):
        """Inits and returns a new Recipe-instance based on the
        information parsed from the given json-object
        @returns the Recipe object"""
        ingrList = []
        for dict in jsonRecipe['ingredients']:
            ingrList.append(Ingredient.ingredientFromJson(dict))
        recipe = Recipe(jsonRecipe['name'], ingrList, jsonRecipe['instructions'])
        return recipe