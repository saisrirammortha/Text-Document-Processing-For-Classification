# Text Document Processing For Classification
* We have used 100 Documents from Newsgroup 20
* We have considered 20 documents from each of five classes of newsgroup20
* We have removed stop words,lemmatized the data and vectorized the words using Word2Vec and applied K means,Louvain,Infomap,Fastgreedy algorithms and checked the validity of clusters using Davies Bouldin and Dunn index
### Implementation
* First, we have formed a vocabulary from 100 Newsgroup Documents after performing basic Pre-processing i.e., Stop Word Removal and Stemming (Porter Stemmer).
* Then we have used Word2Vec to transform each word into a 4-dimensional vector.
* Then we have performed K-means clustering with K=100 on vocabulary.
* We have transformed each document into a 100-dimensional vector where each dimension is equal to number of words of that particular cluster in the document.
* On this data we have performed different Clustering Algorithms
* We have directly applied K-Means using Euclidean Distance as measure.
* But to implement Infomap, Louvain we have used a GML converter.
* We have found the distance between each of the documents.
* Taking average of distance as threshold we have formed a graph.
* The input to the GML converter is the graph formed.

### Issues

This was the code return in the initial stages of my coding.It's not organized.That's why i just explained the steps i have followed
