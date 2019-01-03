from tkinter import * 

mainWindow = Tk()
mainWindow.title("Welcome to project number 18")
mainWindow.geometry('400x400')
instructionsLabelStringVariable = StringVar()
instructionsLabelStringVariable.set("Enter first sentence")

instructionLabel = Label(mainWindow, textvariable=instructionsLabelStringVariable, font=("Arial Bold", 20))

instructionLabel.grid(column=0, row=0)
instructionLabel.pack()

sentenceInputEntryStringVariable = StringVar() # This variable will contain what ever the user has typed into the input field
sentenceInputEntry = Entry(mainWindow, textvariable=sentenceInputEntryStringVariable)
sentenceInputEntry.grid(column=1, row=0)
sentenceInputEntry.focus()
sentenceInputEntry.pack()

S = StringVar()
resultLabels = Label(mainWindow, textvariable=S, font=("Arial Bold", 10))
resultLabels.pack()

Sentences = StringVar()
resultLabel = Label(mainWindow, textvariable=Sentences, font=("Arial Bold", 20))
resultLabel.pack()

result = StringVar()
resultLabel2 = Label(mainWindow, textvariable=result, font=("Arial Bold", 10))
resultLabel2.pack()

a = StringVar()
instructionLabela = Label(mainWindow, textvariable=a, font=("Arial Bold", 10))
instructionLabela.pack()

Snippets1 = StringVar()
#Snippets1 = "snippets value" # put the Snippets output here
Snippets = Label(mainWindow, textvariable=Snippets1, font=("Arial Bold", 20))
Snippets.pack()

b = StringVar()
instructionLabelb = Label(mainWindow, textvariable=b, font=("Arial Bold", 10))
instructionLabelb.pack()

Snippets2 = StringVar()
#Snippets2 = "snippets value" # put the Snippets output here
Snippetsa = Label(mainWindow, textvariable=Snippets2, font=("Arial Bold", 20))
Snippetsa.pack()

c = StringVar()
instructionLabelb = Label(mainWindow, textvariable=c, font=("Arial Bold", 10))
instructionLabelb.pack()

Jaccard = StringVar()
#Jaccard = "Jaccard value" # put the jaccard output here
Jaccard1 = Label(mainWindow, textvariable=Jaccard, font=("Arial Bold", 20))
Jaccard1.pack()

d = StringVar()
instructionLabelb = Label(mainWindow, textvariable=d, font=("Arial Bold", 10))
instructionLabelb.pack()

WordNet = StringVar()
#WordNet = "WordNet value" # put the WordNet output here
WordNet1 = Label(mainWindow, textvariable=WordNet, font=("Arial Bold", 20))
WordNet1.pack()

e = StringVar()
instructionLabelb = Label(mainWindow, textvariable=e, font=("Arial Bold", 10))
instructionLabelb.pack()

Wiki = StringVar()
#Wiki = "Wiki value" # put the Wiki output here
Wiki1 = Label(mainWindow, textvariable=Wiki, font=("Arial Bold", 20))
Wiki1.pack()



numberOfEnteredSentences = 0
S1 = []
S2 = []
S1_2 = []

def submitCallback(): # This function will get called when user presses the 
	S1_2.append(sentenceInputEntryStringVariable.get())
	global numberOfEnteredSentences
	
	numberOfEnteredSentences = numberOfEnteredSentences + 1

	enteredSentence = sentenceInputEntryStringVariable.get()

	if numberOfEnteredSentences == 1:
		S1 = enteredSentence
		print(S1)
	elif numberOfEnteredSentences == 2:
		S2 = enteredSentence
		print(S2)

	sentenceInputEntryStringVariable.set("") # Clear the input field
	instructionsLabelStringVariable.set("Enter second sentence") # Update instructions
	
	if numberOfEnteredSentences == 2:
		# Line below is mock functionality: we should query the api here and then update the result resultLabelStringVariable
		submitButton.pack_forget()
		sentenceInputEntry.pack_forget()
		instructionLabel.pack_forget()
		S.set("Sentences")
		Sentences.set(S1_2)
		result.set("results: ")
		a.set("First Snippets")
		Snippets1.set(Snippets1)
		b.set("Second Snippets")
		Snippets2.set(Snippets2)
		c.set("Jaccard similarity")
		Jaccard.set(Jaccard)
		d.set("WordNet similarity")
		WordNet.set(WordNet)
		e.set("Wiki similarity")
		Wiki.set(Wiki)

submitButton = Button(mainWindow, text="Submit", command=submitCallback)
submitButton.grid(column=6, row=0)
submitButton.pack()

mainWindow.mainloop()
