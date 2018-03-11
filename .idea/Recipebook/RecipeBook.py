import json
from Recipe import Recipe

class RecipeBook:
    """
    A very simple class for a recipebook. Recipebook contains a list of multiple Recipe-objects,
    as well as methods for querying and managing recipes.

    Attributes:
    name: name of the recipebook/library/list
    recipes: list of recipes
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
        try:
            data = json.load(open(file))
            for dict in data:
                self.addRecipe(Recipe.recipeFromJson(json.dumps(dict)))
        except:
            print('The file is either non-excistent, corrupt, empty or incorrectly formatted')
            self.run()


    def searchRecipes(self, searchTerm):
        """an extremely simple search algorithm to find
        recipes by their ingredients"""
        results = []
        for Recipe in self.recipes:
            for Ingredient in Recipe.ingredients:
                if Ingredient.name.lower().find(searchTerm.lower()) is not -1:
                    results.append(Recipe)
                    break
        return json.dumps(results, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4)


    def run(self, fileName=None):
        if fileName is None:
            fileName = input('Enter file name: ')
        self.parseRecipesFromJsonFile(fileName)




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
    test()
   #when testing the stand-alone class, call 'test()' here
#-------------------------------------------------
