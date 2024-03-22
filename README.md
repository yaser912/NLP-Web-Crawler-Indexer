# NLP-Web-Crawler-Indexer
Refined indexing procedure and implementation of ranking returned documents from a given Query



Project Goal: Refine indexing procedure and implement document ranking for query results. Includes two subprojects:

Extraction and Indexing:
Extracts text documents from Reuters 21578 dataset.
Implements SPIMI-inspired inverted index generation during extraction.
Developed query processor to retrieve documents based on user-specified keywords using AND operator.

Ranking Retrieval (Partially Implemented):
Explored BM25 formula for ranking documents.
Tested different parameters (k1, b) for BM25.
Created separate functions for calculating BM25 parameters.
Results ranked and returned for single keyword queries.


Highlights:
Improved indexing efficiency compared to previous project.
SPIMI-inspired procedure significantly reduced processing time.
Query processor successfully retrieves documents based on user keywords.
BM25 formula explored for document ranking.
Challenges encountered with tokenizing words containing non-alphabetical characters.
Importance of ranking highlighted for relevance in retrieval.
Learned efficiency of in-memory inverted index creation.

