from flask import Flask
from flask import request
from RecipeBook import RecipeBook
from Recipe import Recipe
import json


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/getRecipe')
def getRecipe():
    index = request.args.get('index')
    return recipeBook.getRecipeJson(0)

@app.route('/recipes')
def getRecipes():
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
    recipeBook = RecipeBook('Grannys e-recipes')
    recipeBook.run('recipes.json')
    app.run()
