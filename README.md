# nlpminiproject
We have used 100 Documents from Newsgroup 20
We have considered 20 documents from each of five classes of newsgroup20
We have removed stop words,lemmatized the data and vectorized the words using Word2Vec
and applied K means,Louvain,Infomap,Fastgreedy algorithms and checked the validity of clusters using Davies Bouldin and Dunn index

First, we have formed a vocabulary from 100 Newsgroup Document after performing basic Pre-processing i.e., Stop Word Removal and Stemming (Porter Stemmer).


Then we have used Word2Vec to transform each word into a 4-dimensional vector.


Then we have performed K-means clustering with K=100 on vocabulary.

We have transformed each document into a 100-dimensional vector where each dimension is equal to number of words of that particular cluster in the document.

On this data we have performed different Clustering Algorithms

