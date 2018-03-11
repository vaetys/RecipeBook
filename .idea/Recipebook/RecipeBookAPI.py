from flask import Flask
from flask import request
from RecipeBookUI import *
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
    searchTerm = request.args.get('searchTerm')
    return recipeBook.searchRecipes(searchTerm)

@app.route('/addRecipe', methods=['POST'])
def addRecipe():            #DOES NOT WORK
    request.args.get
    return 'Added a new recipe'

    return 'Failed to add new recipe, format might be wrong'


if __name__ == '__main__':
    recipeBook = RecipeBook('Grannys e-recipes')
    recipeBook.run('recipes.json')
    app.run()