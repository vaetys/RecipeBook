from flask import Flask
from flask import request
from RecipeBook import RecipeBook
import json
import sys

#Module to provide a RESTful-API to use the RecipeBook
#this module should only contain the api-handling. Currently
#functions also as the starting module for the application

app = Flask(__name__)

@app.route('/')
def startPage():
    return 'Welcome to the Recipebook API!'

@app.route('/getRecipe')
def getRecipe():
    """Returns a recipe from the given index from param 'index' of RecipeBook.recipes"""
    try:
        index = int(request.args.get('index'))
        return recipeBook.getRecipeJson(index)
    except IndexError:
        return('No recipe in that index') #This is not a sensible solution if developing
                                          #with this API, but works in this case

@app.route('/recipes')
def getRecipes():
    """Returns all recipes from cache"""
    return recipeBook.getRecipesJson()


@app.route('/search')
def search():
    """searches cached recipes, and returns
    a json-list of found recipes. Gets searh term
    from the param 'searchTerm' of the request"""
    searchTerm = request.args.get('searchTerm')
    return recipeBook.searchRecipes(searchTerm)


@app.route('/addRecipe', methods=['POST'])
def addRecipe():
    """Adds a recipe based on the given
    json in the body of the request
    to the cached recipes. Does not write.
    """
    try:
        data = request.get_json(force=True)
        recipeBook.addRecipeFromJson(data)
        return 'Added a new recipe'
    except KeyError:
        return 'Failed to add new recipe, format is wrong'


if __name__ == '__main__':
    recipeBook = RecipeBook('greannys recipes') # Asks for the name of the recipebook. Useless now, but could be used later
    if len(sys.argv) > 1:
       recipeBook.run(sys.argv[1])
    else:
        recipeBook.run(input('Please give filename:'))# Asks for the file to parse. Currently only accepts existing jsons with proper dictionaries
    app.run()