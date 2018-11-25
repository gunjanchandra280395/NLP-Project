# NLP-Project

The aim of this project is to design an approach that makes use of Google and msn snippet in order to compute the semantic similarity between sentences.
Given two sentences S1 and S2, the key is to input each of the sentences to the search engine and investigate the overlapping that may exist between the generated snippets. 
1. Use Google search API and msn search API in order to generate snippets associated to a given sentence. 
2. Retrieve the first ten snippets for each sentence
3. Design and implement a similarity measure that computes the number of overlapping words between the total terms of the ten snippets associated to the first sentence S1 and the first ten snippets associated to the sentence S2. So the similarity here looks similar to Jaccard distance.  You may find the following Msc thesis useful http://www.cs.technion.ac.il/users/wwwb/cgi-bin/tr-get.cgi/2015/MSC/MSC-2015-16.pdf 
4. Start with a simple academic sentences of your choice for S1 and S2 to see how the process works. It is important that you start with sentences with very close meaning and move up to sentences with very disparate meaning (Use a fixed number of pair of sentences of your choice to elaborate your reasoning). Compare the result with sentence semantic similarity that you have seen in Lab2.
5. Refine your code in order to expand the terms of each snippets to include all the hyponyms and hypernyms of the associated words by quering the WordNet database, and repeat the overlapping process.
6. Similarly, use Wikipedia dump files in order to design a program that search the Wikipedia documents for each Sentence. The similarity between the sentences is therefore measured as the number of common Wikipedia documents outputted by the queries (S1 and S2) over the total number of documents outputted by the two queries. Repeat the process of calculating the semantic similarity for your set of chosen academic examples
7. Use a publicly available database of your choice in order to test the usefulness of this similarity measure (Snippets and Wikipedia based similarity) and compare the results with some state of art measures mentioned in the literature employing your chosen publicly database.
8. Design a simple GUI interface that allows you to demonstrate your findings

SUNDAY 25.11.2018 new code example available / Merja / in file NLTK_Assignment_15_test1.py
  It does tokenization steps and calculates jaccard distance.
  Who wants to create code for GUI? 
  But what GUI solution we should use? 


