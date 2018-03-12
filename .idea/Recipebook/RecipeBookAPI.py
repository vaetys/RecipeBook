from flask import Flask
from flask import request
from RecipeBook import RecipeBook
from Recipe import Recipe
import json

#Module to provide a RESTful-API to use the RecipeBook
#this module should only contain the api-handling. Currently
#functions also as the starting module for the application

app = Flask(__name__)

@app.route('/')
def startPage():
    return 'Welcome to the Recipebook API!'

@app.route('/getRecipe')
def getRecipe():
    """Returns a recipe from the given index of RecipeBook.recipes"""
    index = request.args.get('index')
    return recipeBook.getRecipeJson(0)


@app.route('/recipes')
def getRecipes():
    """Returns all recipes from cache"""
    return recipeBook.getRecipes()


@app.route('/search')
def search():
    """searches cached recipes, and returns
    a json-list of found recipes"""
    searchTerm = request.args.get('searchTerm')
    return recipeBook.searchRecipes(searchTerm)


@app.route('/addRecipe', methods=['POST'])
def addRecipe():
    try:
        """Adds a recipe based on the given json
        to the cached recipes. Does not write it"""
        data = request.get_json(force=True)
        recipeBook.addRecipeFromJson(data)
        return 'Added a new recipe'
    except KeyError:
        return 'Failed to add new recipe, format is wrong'



if __name__ == '__main__':
    recipeBook = RecipeBook('greannys recipes') # Asks for the name of the recipebook. Useless now, but could be used later
    recipeBook.run('recipes.json')  # Asks for the file to parse. Currently only accepts existing jsons with proper dictionaries
    app.run()


