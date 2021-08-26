from tkinter import *
from generateRecipes import generateRecipes
import random

class Gui:
    root = Tk()
    promptFrame = LabelFrame(root, text="Hello, how many meals would you like to cook this week? (1-5)")
    recipeFrame = LabelFrame(root, text="Here are your suggested recipes")

    def startGui(self):
        print("hfwew")
        self.showPromptFrame()
        self.root.geometry("500x300")
        self.root.mainloop()

    def showPromptFrame(self):
        self.promptFrame = LabelFrame(self.root, text="Hello, how many meals would you like to cook this week? (1-5)")

        promptEntry = Entry(self.promptFrame)
        promptEntry.pack()

        nextButton = Button(self.promptFrame, text="Next", command=self.nextButton, highlightbackground='#3E4149')
        nextButton.pack()

        self.promptFrame.pack()

    def showRandomRecipeFrame(self):
        self.recipeFrame = LabelFrame(self.root, text="Here are your suggested recipes")

        numberOfMeals = 5
        recipeLabelList = []

        recipeList = generateRecipes()
        randomRecipeList = random.sample(recipeList, numberOfMeals)

        for recipe in randomRecipeList:
            recipeLabelList.append(Label(self.recipeFrame, text=recipe.name))
            print(recipe.name)

        for recipeLabel in recipeLabelList:
            recipeLabel.pack()

        backButton = Button(self.recipeFrame, text="Back", command=self.backButton, highlightbackground='#3E4149')

        backButton.pack()

        self.recipeFrame.pack()

    def backButton(self):
        self.recipeFrame.destroy()
        self.showPromptFrame()

    def nextButton(self):
        self.promptFrame.destroy()
        self.showRandomRecipeFrame()








# print("hello")
# gui = Gui()
# gui.startGui()

