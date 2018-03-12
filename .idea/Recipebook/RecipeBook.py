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
        if recipes is None:
            self.recipes = []
        else:
            self.recipes=recipes


    def addRecipe(self, recipe):
        """Adds a single Recipe to the Recipebook.recipes"""
        self.recipes.append(recipe)


    def getRecipeJson(self, index):
        """gets a single Recipe from the Recipebook.recipes with the give index"""
        return self.recipes[index].toJSON()

    def getRecipes(self):
        """Returns the Recipebook.recipes as a json-object"""
        return json.dumps(self.recipes, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4)


    def parseRecipesFromJsonFile(self, file):
        """Parses the given json-file, creates Recipe-instances and appends the to Recipebook.recipes"""

        data = json.load(open(file))
        for dict in data:
            self.addRecipe(Recipe.recipeFromJson(dict))



    def searchRecipes(self, searchTerm):
        """Returns a json-fobject list of recipes,
        where any of its ingredients contain the given
        searchTerm"""
        results = []
        for Recipe in self.recipes:
            for Ingredient in Recipe.ingredients:
                if Ingredient.name.lower().find(searchTerm.lower()) is not -1: #if the ingredient name contains the searchterm
                    results.append(Recipe)
                    break
        return json.dumps(results, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4)


    def run(self, fileName=None):
        if fileName is None:
            fileName = input('Enter file name: ')
        self.parseRecipesFromJsonFile(fileName)

    def addRecipeFromJson(self, json):
        """creates and adds a recipe from json-object
        the object must be properly formatted with corresponding keys"""

        recipe = Recipe.recipeFromJson(json)
        self.addRecipe(recipe)



#THIS IS A TESTING BLOCK
#-------------------------------------------------
def test():
    testlist = RecipeBook('myRecipes')
    testlist.run('recipes.json')
    recipe1 = Recipe('rice pudding')
    testlist.addRecipe(recipe1)

    recipe2 = testlist.getRecipeJson(0)

    print(testlist.searchRecipes('chIcken'))

if __name__ == '__main__':
    pass
    # test()
   #when testing the stand-alone class, call 'test()' here
#-------------------------------------------------
