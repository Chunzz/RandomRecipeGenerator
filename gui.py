from tkinter import *
from generateRecipes import generateRecipes
import random
from tkinter import messagebox

class Gui:
    root = Tk()
    promptFrame = LabelFrame(root, text="Hello, how many meals would you like to cook this week? (1-5)")
    promptEntry = Entry(promptFrame)
    recipeFrame = LabelFrame(root, text="Here are your suggested recipes")
    userSelectionFrame = LabelFrame(root, text="Hello, please select a user")
    numberOfRecipe = 0
    userId = 0

    def startGui(self):
        self.showUserSelectionFrame()
        self.root.geometry("500x300")
        self.root.mainloop()

    def showUserSelectionFrame(self):
        self.userSelectionFrame = LabelFrame(self.root, text="Hello, please select a user")
        samButton = Button(self.userSelectionFrame, text="Sam", command=self.samButton, highlightbackground='#3E4149')
        samButton.pack()
        ariefButton = Button(self.userSelectionFrame, text="Arief", command=self.ariefButton, highlightbackground='#3E4149')
        ariefButton.pack()
        self.userSelectionFrame.pack()



    def showPromptFrame(self):
        if self.userId == 0:
            promptText = "Hi Arief, how many meals would you like to cook this week? (1-5)"
        else:
            promptText = "Hi Sam, how many meals would you like to cook this week? (1-5)"


        self.promptFrame = LabelFrame(self.root, text=promptText)
        self.promptEntry = Entry(self.promptFrame)
        self.promptEntry.pack()


        backButtonOne = Button(self.promptFrame, text="Back", command=self.backButtonOne, highlightbackground='#3E4149')
        backButtonOne.pack()

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

    def samButton(self):
        self.userId = 1
        self.userSelectionFrame.destroy()
        self.showPromptFrame()

    def ariefButton(self):
        self.userId = 0
        self.userSelectionFrame.destroy()
        self.showPromptFrame()

    def backButtonOne(self):
        self.promptFrame.destroy()
        self.showUserSelectionFrame()

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




