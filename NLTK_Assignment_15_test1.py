# NLTK Assignment 15

# NLTK code

import nltk
import string
import math 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.porter import PorterStemmer
import pandas as pd
import re

# load / import text ##########
# filename = 'our data'
# file = open(filename, 'rt')
# text = file.read()
# file.close()

# import data from csv file ##########
# import pandas as pd
# snippets = pd.read_csv('filename or address', header=None)
# snippets()


# snippets examples ##########

document_1 = "It is easy to add code snippets to Visual Studio Code both for your own use or to share with others on the public Extension Marketplace. TextMate .tmSnippets "
document_2 = " You can create a code snippet with only a few steps. All you need to do is create an XML file, fill in the appropriate elements, and add your code ..."
document_3 = " Generate code snippets. Once you’ve finalized and saved your request in Postman, you might want to make the same request from your own application."
document_4 = "Creating your own snippets. Code snippets are templates that make it easier to enter repeating code patterns, such as loops or conditional-statements. "

all_documents = [document_1, document_2, document_3, document_4]

print('All Snippets')
for allCase in all_documents:
    allStr = allCase + "\n"
    print(allStr)



low_documents = []
for document in all_documents:
    low_documents.append(document.lower())
print('lower case snippets')
for lowCase in low_documents:
    lowStr = lowCase + "\n"
    print(lowStr)

# tokenization by split ##################

print('Sentences Tokenized into Words (split by whitespace)')
sentences_documents = []
for document in low_documents:
    sentences_documents.append(document.split())
print(sentences_documents)


# change compound words to separate words ie. 'conditional-statements' -> 'conditional', 'statements' 
single_word_documents = []
for sentence_words in sentences_documents:
    single_word_list = []
    for word in sentence_words:
        regex = re.compile("[-_]")
        trimmed = regex.sub(' ', word)
        separate = trimmed.split( )
        for item in separate:
            single_word_list.append(item)        
    single_word_documents.append(single_word_list)
print(single_word_documents)

# remove all tokens that are not alphabetic #############
print('Tokenized with alphabetic chars only')
alpha_documents = []
for single_word_sentence in single_word_documents:
    cleaned_list = []
    for single_word in single_word_sentence:
        regex = re.compile('[^a-zA-Z]')
        #First parameter is the replacement, second parameter is your input string
        nonAlphaRemoved = regex.sub('', single_word)
        # add string to list only if it has content
        if nonAlphaRemoved:
            cleaned_list.append(nonAlphaRemoved)
    alpha_documents.append(cleaned_list)
print(alpha_documents)



# filter out stopwords ########
print('English stopwords filtered tokens')
stop_filtered_tokens = []
english_stop_words = set(stopwords.words('english'))

for fword in alpha_documents:
    fword_list = []
    for sword in fword:
        #fword_list = [sword for sword in alpha_documents if not sword in english_stop_words]
        if not sword in english_stop_words:
            fword_list.append(sword)
    stop_filtered_tokens.append(fword_list)
print(stop_filtered_tokens)  


# tokenization by PorterStemmer ############
print('Word Stemming by PorterStemmer')
porter_documents = []
for ps_word_list in stop_filtered_tokens:
    PS = PorterStemmer()
    porter_list = []
    for ps_word in ps_word_list:
        porter_list.append(PS.stem(ps_word))
    porter_documents.append(porter_list)
print(porter_documents)


# define jaccard similarity for python ################
def jaccard_similarity(query, jdoc):
    intersection = set(query).intersection(set(jdoc))
    union = set(query).union(set(jdoc))
    return len(intersection)/len(union)

# calculate jaccard similarity
print('Jaccard similarity')
result = jaccard_similarity(porter_documents[0], porter_documents[1])
j_string = "{:.4f}".format(result)
print(j_string)



