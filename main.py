import random
from generateRecipes import generateRecipes
from gui import *



# while True:
#     # How many meals would you like to cook (1-5)?
#     numberOfMeals = int(input("\nHow many meals would you like to cook? (1-5): "))
#
#     #User Validation
#     if numberOfMeals > 5:
#         print("Too many meals entered, try a smaller number")
#     elif numberOfMeals <= 0:
#         print("Invalid number, try another number (1-5)")
#     else:
#         break
#
#
# #Generate random meals
# recipeList = generateRecipes()
# randomRecipeList = random.sample(recipeList, numberOfMeals)
# for recipe in randomRecipeList:
#     print(recipe.name)

#Display GUI'
print("hello")
gui = Gui()
gui.startGui()