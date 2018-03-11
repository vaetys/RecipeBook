from Recipe import Recipe
from Ingredient import Ingredient
from RecipeBook import RecipeBook
import click


# This is a work in progress to create a
# terminal user interface using click-library
#

@click.group()
def run(name):
    pass


@run.command()
@click.option('--name', prompt='your name',
              help='Your own name!')
def greet(name=None):
    """greets the user"""
    click.echo("hello %s" % name)


@click.command()
def moi():
    click.echo("NO MOI")

def showRecipe():
    Recipe



if __name__ == "__main__":
    run()

