from tkinter import * 

mainWindow = Tk()
mainWindow.title("Welcome to project number 18")
mainWindow.geometry('350x200')

# State
numberOfEnteredSentences = 0
S1 = []
S2 = []

# Insert sentences layout string variables
instructionsLabelStringVariable = StringVar()
instructionsLabelStringVariable.set("Enter first sentence")
resultLabelStringVariable = StringVar()
sentenceInputEntryStringVariable = StringVar() # This variable will contain what ever the user has typed into the input field
result = StringVar()

# Results layout string variables
resultsFirstSentenceStringVariable = StringVar()
resultsFirstSentenceStringVariable.set("First sentence")
resultsSecondSentenceStringVariable = StringVar()
resultsSecondSentenceStringVariable.set("Second sentence")
resultsFirstSnippetsStringVariable = StringVar()
resultsFirstSnippetsStringVariable.set("Here be first snippet")
resultsSecondSnippetsStringVariable = StringVar()
resultsSecondSnippetsStringVariable.set("Here be second snippet")
resultsWordNetSimilarityStringVariable  = StringVar()
resultsWordNetSimilarityStringVariable.set("Over 9000")
resultsWikiSimilarityStringVariable  = StringVar()
resultsWikiSimilarityStringVariable.set("Over 9001")
# Callbacks
def submitCallback(): # This function will get called when user presses the 
	global numberOfEnteredSentences, S1, S2
	
	numberOfEnteredSentences = numberOfEnteredSentences + 1

	enteredSentence = sentenceInputEntryStringVariable.get()

	if numberOfEnteredSentences == 1:
		S1 = enteredSentence
	elif numberOfEnteredSentences == 2:
		S2 = enteredSentence

	sentenceInputEntryStringVariable.set("") # Clear the input field
	instructionsLabelStringVariable.set("Enter second sentence") # Update instructions
	
	if numberOfEnteredSentences == 2:
		# Line below is mock functionality: we should query the api here and then update the result resultLabelStringVariable
		result.set("test: ")
		resultLabelStringVariable.set("blaablaa")
		removeInsertSentencesLayout()
		displayResultsLayout()

# Insert sentences layout elements
instructionLabel = Label(mainWindow, text="Enter the first sentence:", textvariable=instructionsLabelStringVariable, font=("Arial Bold", 20))
resultLabel2 = Label(mainWindow, textvariable=result)
resultLabel = Label(mainWindow, text="Result:", textvariable=resultLabelStringVariable)
sentenceInputEntry = Entry(mainWindow, textvariable=sentenceInputEntryStringVariable)
submitButton = Button(mainWindow, text="Submit", width=10, command=submitCallback)


def displayInsertSentencesLayout():	
	instructionLabel.grid(column=0, row=0)
	instructionLabel.pack()
	
	sentenceInputEntry.grid(column=1, row=0)
	sentenceInputEntry.focus()
	sentenceInputEntry.pack()
	
	resultLabel2.pack()
	
	resultLabel.grid(column=2, row=0)
	resultLabel.pack()
	
	submitButton.grid(column=3, row=0)
	submitButton.pack()


def removeInsertSentencesLayout():
	instructionLabel.pack_forget()
	sentenceInputEntry.pack_forget()
	resultLabel2.pack_forget()
	resultLabel.pack_forget()
	submitButton.pack_forget()


def displayResultsLayout():
	# Update labels
	resultsFirstSentenceStringVariable.set(S1)
	resultsSecondSentenceStringVariable.set(S2)

	# Layout elements
	Label(mainWindow, text="S1", font=("Arial Bold", 20)).grid(row=0, column=0)
	Label(mainWindow, text="S2", font=("Arial Bold", 20)).grid(row=0, column=1)

	Label(mainWindow, textvariable=resultsFirstSentenceStringVariable).grid(row=1, column=0)
	Label(mainWindow, textvariable=resultsSecondSentenceStringVariable).grid(row=1, column=1)

	Label(mainWindow, text="Snippets", font=("Arial Bold", 20)).grid(row=2, column=0)
	Label(mainWindow, textvariable=resultsFirstSnippetsStringVariable).grid(row=3, column=0)
	Label(mainWindow, textvariable=resultsSecondSnippetsStringVariable).grid(row=3, column=1)

	Label(mainWindow, text="WordNet similarity", font=("Arial Bold", 20)).grid(row=4, column=0)
	Label(mainWindow, textvariable=resultsWordNetSimilarityStringVariable).grid(row=5, column=0)

	Label(mainWindow, text="Wiki similarity", font=("Arial Bold", 20)).grid(row=6, column=0)
	Label(mainWindow, textvariable=resultsWordNetSimilarityStringVariable).grid(row=7, column=0)

displayInsertSentencesLayout()
mainWindow.mainloop()
