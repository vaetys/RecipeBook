from Recipe import Recipe
from Ingredient import Ingredient
from RecipeBook import RecipeBook
import click
import RecipeBookAPI


# This is a work in progress to create a
# terminal user interface using click-library
#

def run():

    pass


@click.command()
@click.option('--name', '-n', prompt='your name',
              help='Your own name!')
def greet(name=None):
    """greets the user"""
    click.echo("hello %s" % name)


@click.command()
def moi():
    click.echo("NO MOI")


def showRecipe():
    Recipe

@click.command()
def startApi():
    RecipeBookAPI.run()
    click.echo('\n Stopped the Recipebook API \n')


if __name__ == "__main__":
    run()



