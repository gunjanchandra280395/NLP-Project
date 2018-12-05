import requests 
import nltk as nltk
from array import array
import json 
import tkinter
from tokenize import tokenize
import nltk
import string
import math 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.porter import PorterStemmer
import pandas as pd
import re
import sys
import numpy

#str = input("Enter your input: ");
#print("Received input is : ", str)


#top = tkinter.Tk()









#def Submit():
   #tkMessageBox.showinfo( "Hello Python", "Hello World")

#B = tkinter.Button(top, text ="Analyse", command = Submit)

#B.pack()

#top.mainloop()


Query = ['i love python','i hate python']
#Query = []
#Query.append(input("Enter 1st sentence: "))
#Query.append(input("Enter 2nd sentence: "))
response_1 = requests.get("https://www.googleapis.com/customsearch/v1?key='add your own key'&cx=012278024424817052234:cimrvj4h4uk&q="+Query[0])

#print(Query)
#print(response)

data_1 = response_1.json()


#data = tokenize(data_1);
#print(data)

#
##print(data_1)
items_1 = data_1["items"]
snippets_1 = []
for index in range(0,len(items_1)):
	snippets_1.extend(items_1[index]["snippet"].split(" "))
#	snippets_1.append(items_1[index]["snippet"])
#snippets_1 = snippets_1.replace(u'\xa0', u' ')
##snippets_1 = snippets_1.replace(u'\n', u' ')
#
print(snippets_1)
#
response_2 = requests.get("https://www.googleapis.com/customsearch/v1?key=AIzaSyDm4968sAb9h94I1b37wPvNi2FlpIhxRzE&cx=012278024424817052234:cimrvj4h4uk&q="+Query[1])
data_2 = response_2.json()
items_2 = data_2["items"]
snippets_2 = []
for index in range(0,len(items_2)):
	snippets_2.append(items_2[index]["snippet"])
#
##snippets_2 = snippets_2.replace(u'\xa0', u' ')
##snippets_2 = snippets_2.replace(u'\n', u' ')
#
print(snippets_2)




#print(data_1)

#data_2 = response_2.json()
#print(data_2)

#'What are snippets?','how to generate snippets?'





#https://www.googleapis.com/customsearch/v1?key=AIzaSyDOvbipdULbUpVm3HLjoX7bEEfDUKHELh4&cx=012278024424817052234:cimrvj4h4uk&q=What are snippets?
#
#
#
#
#data_all = pd.DataFrame(snippets_1)
#data_all.columns = ['Academic sentence - short example']
##display(data_all.head())  
#
#low_documents = []
#for document in snippets_1:
#    low_documents.append(document.lower())
#    
#data_low = pd.DataFrame(low_documents)
#data_low.columns = ['Lower case sentence']
##display(data_low.head())  
#    
## tokenization by split # Sentences Tokenized into Words - split by whitespace
#
#sentences_documents = []
##document_counter = 0
#for document in low_documents:
#    sentences_documents.append(document.split())
#
#printableList1 = []
#for sentence1 in sentences_documents:
#    sentence1AsString = ''
#    for idx1, aWord1 in enumerate(sentence1):        
#        if idx1 == len(sentence1) - 1:
#            sentence1AsString = sentence1AsString + aWord1
#        else:
#            str1 = aWord1 + ', '
#            sentence1AsString = sentence1AsString + str1
#    printableList1.append(sentence1AsString)
#
#data_sentences1 = pd.DataFrame(printableList1)
#data_sentences1.columns = ['Sentence tokenized into words   - string form and comma separated for display']
##display(data_sentences1.head())
#
#print("\n" 'Single words' "\n")
#single_word_documents = []
#for sentence_words in sentences_documents:
#    single_word_list = []
#    for word in sentence_words:
#        regex = re.compile("[-_]")
#        trimmed = regex.sub(' ', word)
#        separate = trimmed.split( )
#        for item in separate:
#            single_word_list.append(item)        
#    single_word_documents.append(single_word_list)
#print(single_word_documents)
#
#printableList2 = []
#for sentence2 in single_word_documents:
#    sentence2AsString = ''
#    for idx2, aWord2 in enumerate(sentence2):        
#        if idx2 == len(sentence2) - 1:
#            sentence2AsString = sentence2AsString + aWord2
#        else:
#            str2 = aWord2 + ', '
#            sentence2AsString = sentence2AsString + str2
#    printableList2.append(sentence2AsString)
#
#data_sentences2 = pd.DataFrame(printableList2)
#data_sentences2.columns = ['Single words   - string form and comma separated for display']
##display(data_sentences2.head())      
#    
#    
#    
## remove all tokens that are not alphabetic #############
#print("\n" 'Tokenized with alphabetic chars only' "\n")
#alpha_documents = []
#for single_word_sentence in single_word_documents:
#    cleaned_list = []
#    for single_word in single_word_sentence:
#        regex = re.compile('[^a-zA-Z]')
#        #First parameter is the replacement, second parameter is your input string
#        nonAlphaRemoved = regex.sub('', single_word)
#        # add string to list only if it has content
#        if nonAlphaRemoved:
#            cleaned_list.append(nonAlphaRemoved)
#    alpha_documents.append(cleaned_list)
#print(alpha_documents)
#
#printableList3 = []
#for sentence3 in alpha_documents:
#    sentence3AsString = ''
#    for idx3, aWord3 in enumerate(sentence3):        
#        if idx3 == len(sentence3) - 1:
#            sentence3AsString = sentence3AsString + aWord3
#        else:
#            str3 = aWord3 + ', '
#            sentence3AsString = sentence3AsString + str3
#    printableList3.append(sentence3AsString)
#
#data_sentences3 = pd.DataFrame(printableList3)
#data_sentences3.columns = ['Tokenized with alphabetic chars only   - string form and comma separated for display']
##display(data_sentences3.head())     
#
#
## filter out stopwords ########
#print("\n" 'English stopwords filtered tokens' "\n")
#stop_filtered_tokens = []
#english_stop_words = set(stopwords.words('english'))
#
#for fword in alpha_documents:
#    fword_list = []
#    for sword in fword:
#        #fword_list = [sword for sword in alpha_documents if not sword in english_stop_words]
#        if not sword in english_stop_words:
#            fword_list.append(sword)
#    stop_filtered_tokens.append(fword_list)
#print(stop_filtered_tokens)  
#
#
#printableList4 = []
#for sentence4 in stop_filtered_tokens:
#    sentence4AsString = ''
#    for idx4, aWord4 in enumerate(sentence4):        
#        if idx4 == len(sentence4) - 1:
#            sentence4AsString = sentence4AsString + aWord4
#        else:
#            str4 = aWord4 + ', '
#            sentence4AsString = sentence4AsString + str4
#    printableList4.append(sentence4AsString)
#
#data_sentences4 = pd.DataFrame(printableList4)
#data_sentences4.columns = ['English stopwords filtered tokens   - comma separated for display']
##display(data_sentences4.head())     
#
#
## tokenization by PorterStemmer ############
#print("\n" 'Word Stemming by PorterStemmer' "\n")
#porter_documents = []
#for ps_word_list in stop_filtered_tokens:
#    PS = PorterStemmer()
#    porter_list = []
#    for ps_word in ps_word_list:
#        porter_list.append(PS.stem(ps_word))
#    porter_documents.append(porter_list)
#print(porter_documents)
#
#printableList5 = []
#for sentence5 in porter_documents:
#    sentence5AsString = ''
#    for idx5, aWord5 in enumerate(sentence5):        
#        if idx5 == len(sentence5) - 1:
#            sentence5AsString = sentence5AsString + aWord5
#        else:
#            str5 = aWord5 + ', '
#            sentence5AsString = sentence5AsString + str5
#    printableList5.append(sentence5AsString)
#
#data_sentences5 = pd.DataFrame(printableList5)
#data_sentences5.columns = ['Word Stemming by PorterStemmer   - comma separated for display']
##display(data_sentences5.head())
#
#
#
#
#
#
#
#
#
## define jaccard similarity for python ################
#def jaccard_similarity(query, jdoc):
#    intersection = set(query).intersection(set(jdoc))
#    union = set(query).union(set(jdoc))
#    return len(intersection)/len(union)
#
## calculate jaccard similarity
#print('Jaccard similarity')
#result = jaccard_similarity(porter_documents[0], porter_documents[1])
#j_string = "{:.4f}".format(result)
#print(j_string)
#
#
##data_table1 = pd.DataFrame(tableJaccSim1)
## data_table1.columns = ['n', 'sentence', 'n', 'sentence', 'JaccardSim'  ]
##display(data_table1.head())
#
#def listToString (sourceList):
#    subListAsString = ''    
#    for listIndex, listWord in enumerate(sourceList):        
#        if listIndex == len(sourceList) - 1:
#            subListAsString = subListAsString + listWord
#        else:
#            strWithComma = listWord + ', '
#            subListAsString = subListAsString + strWithComma        
#    return subListAsString
#
## compare the first porter document to the rest in the porter docs list
#def printJaccardSimilarities (porterDocs):    
#    printableJaccardList = []    
#    for porterIndex, porter in enumerate(porterDocs):
#        if porterIndex > 0:            
#            jresult = jaccard_similarity(porterDocs[0], porter)    
#            j_string = "{:.4f}".format(jresult)
#            porterParamStr1 = listToString(porterDocs[0])
#            porterParamStr2 = listToString(porter)
#            data = [0, porterParamStr1, porterIndex, porter, j_string]
#            printableJaccardList.append(data)
#    df = pd.DataFrame(printableJaccardList,columns=['First Index','First Sentence','Second Index','Second Sentence','Jaccard similarity'])
#    #display(df.head()) 
#
#printJaccardSimilarities(porter_documents)#