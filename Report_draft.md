Analysis of Snippets


Abstract: The objective of the project was to design and understand an approach that uses Google, Msn and, Youtube snippets in order to compute the semantic similarity between snippets using similarity measures such as overlapping words which is similar to Jaccard similarity, using wikipedia dump files for finding the number of same documents for two given sentences, Sentence semantic similarity algorithm using WordNet etc. 


The two sentences are used S1 and S2 for evaluation process of the system. Initially these two sentences are used to generate 10 snippets for each sentences. Investigation is taken place by measuring the overlapping if that exist between the snippets generated using sentences.


Many challenges were faced during the design, deployment and, evaluation process. 


Technologies: Technologies used for this project can be divided into three parts. 1. Data Sources: Google Custom search API, Msn Bing search API v7, WordNet, Wikipedia Dump Files, Youtube API. 2. Tools: Python Programming, NLTK, Gensim, TKinter, pandas etc., Visual Studio Code, Sublime Text. 3. Communication and documentation: Github, Jupyter Notebook, E-mail, Whatsapp, PowerPoint, MS word, and Pages. 


Task 1 and 2: Generating and retrieving snippets: 


Snippets are a small piece or brief extract of a given word or sentence. In this project we are using 3 different types of databases to generate snippets. To generate snippets we are using Google API and msn API with python programming language. Google APIs is a set of application programming interfaces (APIs) developed by Google which allow communication with Google Services and their integration to other services. Same goes for msn APIs. In order to generate snippets, set of commands were used to call the server and retrieve data and Json formatting was used to retrieve only wanted data which was snippets. 


Snippets are generated for a word or a sentence. In our case we are using 2 academic sentences in the beginning with similar meaning. Before feeding the sentences into the system to generate snippet we first parse it through a process called preprocessing which includes Tokenization, Removal of stop words, Stemming. After preprocessing the collection of words are feed into the API call and corresponding snippets are generated. 


Tokenization is the act of breaking up a sequence of strings into pieces such as words, keywords, phrases, symbols and other elements called tokens. In the process of tokenization, some characters like punctuation marks are discarded. The tokens become the input for another process which is Removal of stop word. Stop words are natural language words which have very little meaning, such as "and", "the", "a", "an", and similar words. These words are removed but the removal of stop words may or may not increase the performance of your model. In our case stop words were removed for very specific evaluation. Stemming is done to generalise the text and finally special characters were removed as well. 


One issue which was faced during snippets generation was that every sentences were not generating 10 snippets for each sentences. Many theory were discussed in order to evaluate the issue and find a solution. One of which was when API call is made text from the search is retrieved but when the text is large then page needs to be scrolled down in order to load more snippets therefore small and easy sentences were used so the snippets will be short and more text can be retrieved. 


Two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes were used for better access to the data. After the snippets have been generated later these documents were parsed through the process call post-processing which includes Tokenization, Removal of stop words, Stemming and removal of special character for above mentioned reasons.

Task 2: In this task we supposed to Design and implement a similarity measure between the two sentences S1 and S2 using a similarity measure which is calculated by the number of overlapping words in the collection of words which was created using snippets of two initial sentences. Number or overlapping means the number of words which exist in both the sets will be considered. Similarity measure by overlapping of words can also be mentioned as Jaccard similarity distance. In other words, The Jaccard coefficient measures similarity between finite sample sets, and is defined as the size of the intersection divided by the size of the union of the sample sets. 

We are using a predefined function for calculating Jaccard similarity which take input the collection of words and outputs the number of similarity (number of overlapping words in two different sets). 

Task 3: We used the academic sentences which are similar in meaning during deployment process and for tasing and evaluating the errors and then  progressed for sentences which were distinct in meaning to test the performance of the system. 





