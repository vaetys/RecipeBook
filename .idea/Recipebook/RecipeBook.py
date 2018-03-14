import json
from Recipe import Recipe
from Ingredient import Ingredient

class RecipeBook:
    """
    A very simple class for a recipebook. Recipebook contains a list of multiple Recipe-objects,
    as well as methods for querying and managing recipes.

    Attributes:
        name: name of the recipebook
        recipes: list of recipes as in Recipe-objects
    """

    def __init__(self, name=None, recipes=None):
        self.name = name
        if recipes is None: #If a ready list is not given, creates an empty list to use
            self.recipes = []
        else:
            self.recipes=recipes


    def addRecipe(self, recipe):
        """Adds a single Recipe to the Recipebook.recipes"""
        self.recipes.append(recipe)


    def getRecipeJson(self, index):
        """@returns a single Recipe from the Recipebook.recipes with the give index"""
        return self.recipes[index].toJson()


    def getRecipesJson(self):
        """@returns the Recipebook.recipes as a json-object"""
        return json.dumps(self.recipes, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4)


    def parseRecipesFromJsonFile(self, file):
        """Parses the given json-file, creates Recipe-instances and appends the to Recipebook.recipes"""
        try:
            data = json.load(open(file))
            for dict in data: # Loops through each dictionary in the file
                self.addRecipe(Recipe.recipeFromJson(dict)) #Inits a recipe, and adds it to the recipebook
        except (FileNotFoundError, ValueError, KeyError) as e:
            newFilename = input('File with that name not found or is empty, try another:')
            self.run(newFilename)


    def searchRecipes(self, searchTerm):
        """Returns a json-object list of recipes,
        where any of its ingredients contain the given
        searchTerm
        @returns json-list of found recipes"""
        results = []
        for Recipe in self.recipes:
            for Ingredient in Recipe.ingredients:
                if Ingredient.name.lower().find(searchTerm.lower()) is not -1: #if the ingredient name contains the searchterm
                    results.append(Recipe)
                    break
        return json.dumps(results, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4) # Parses the results-list into json


    def run(self, fileName):
        """Basically 'runs' the app. Currently only starts by reading the given file"""
        self.parseRecipesFromJsonFile(fileName)


    def addRecipeFromJson(self, json):
        """creates and adds a recipe from json-object
        the object must be properly formatted with corresponding keys"""
        recipe = Recipe.recipeFromJson(json)
        self.addRecipe(recipe)



#THIS IS A TESTING BLOCK
#-------------------------------------------------
def test():
    pass

if __name__ == '__main__':
    pass
    # test()
   #when testing the stand-alone class, call 'test()' here
#-------------------------------------------------
