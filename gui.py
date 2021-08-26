from tkinter import *
from generateRecipes import generateRecipes
import random
from tkinter import messagebox

class Gui:
    root = Tk()
    promptFrame = LabelFrame(root, text="Hello, how many meals would you like to cook this week? (1-5)")
    promptEntry = Entry(promptFrame)
    recipeFrame = LabelFrame(root, text="Here are your suggested recipes")
    numberOfRecipe = 0

    def startGui(self):
        self.showPromptFrame()
        self.root.geometry("500x300")
        self.root.mainloop()

    def showPromptFrame(self):
        self.promptFrame = LabelFrame(self.root, text="Hello, how many meals would you like to cook this week? (1-5)")
        self.promptEntry = Entry(self.promptFrame)
        self.promptEntry.pack()
        nextButton = Button(self.promptFrame, text="Next", command=self.nextButton, highlightbackground='#3E4149')
        nextButton.pack()
        self.promptFrame.pack()

    def showRecipeFrame(self):
        self.recipeFrame = LabelFrame(self.root, text="Here are your suggested recipes\n")
        recipeLabelList = []
        recipeList = generateRecipes()
        randomRecipeList = random.sample(recipeList, self.numberOfRecipe)

        for recipe in randomRecipeList:
            recipeLabelList.append(Label(self.recipeFrame, text=recipe.name))

        for recipeLabel in recipeLabelList:
            recipeLabel.pack()

        backButton = Button(self.recipeFrame, text="Back", command=self.backButton, highlightbackground='#3E4149')
        backButton.pack()

        regenerateButton = Button(self.recipeFrame, text="Regenerate", command=self.regenerateButton, highlightbackground='#3E4149')
        regenerateButton.pack()

        self.recipeFrame.pack()

    def regenerateButton(self):
        self.recipeFrame.destroy()
        self.showRecipeFrame()

    def backButton(self):
        self.recipeFrame.destroy()
        self.showPromptFrame()

    def nextButton(self):
        try:
            value = self.promptEntry.get()
            self.numberOfRecipe = int(value)

            if self.numberOfRecipe <=0 or self.numberOfRecipe >5:
                messagebox.showerror('Python Error', "Please enter a valid number (1-5)")
            else:
                self.promptFrame.destroy()
                self.showRecipeFrame()

        except ValueError:
            messagebox.showerror('Python Error', "Please enter a valid number (1-5)")




