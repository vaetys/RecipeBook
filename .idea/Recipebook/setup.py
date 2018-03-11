from setuptools import setup


setup(name="Recipe Book",
      version='1.0',
      py_modules=['RecipeBookAPI',
                  'Recipe',
                  ],
      install_requires=[
          'Click',
      ],
      entry_points="""
        [console_scripts]
        hello=RecipeBookUI:greet
        """,
      )