import subproject1
import math


def calculate_doc_frequency(term):
    # Initialize a dictionary to store document frequencies
    frequency = 0
    # Iterate through the document dictionary
    for doc_id, document_text in subproject1.documents.items():
        if term in document_text:  # if term is in dictionary, return count of frequency of term
            frequency = document_text.count(term)
    return frequency


def calculate_term_frequency(term, document_for_term):
    term_frequencies = {}
    final_tf = 0
    for doc_id, document_text in subproject1.documents.items():
        # seperate words into segments using split()
        words = document_text.split()
        # Count the occurrences of the term in the list of words using count()
        termFrequency = words.count(term)

        term_frequencies[doc_id] = termFrequency

    for doc_id, tf in term_frequencies.items():
        # print(f"Document {doc_id}: Term frequency of '{term}' is {tf}")
        if doc_id == str(document_for_term):
            final_tf += tf
    return final_tf


def calculate_average_length():
    # Initialize variables for sum of document lengths and the total number of documents
    total_length = 0
    total_documents = len(subproject1.documents)

    # Calculate the sum of document lengths
    for document_text in subproject1.documents.values():
        total_length += len(document_text.split())  # Assuming you split text by spaces

    # Calculate the average document length (Lave)
    Lave = total_length / total_documents

    return Lave


query = input("Please enter your query: ")
queries = []
queries.append(query)

# I will be using values 1.2 and 0.5 for testing
N = len(subproject1.documents)  # Total number of documents
k1 = 1.5
b = 1

# dictionary to store RSVd scores for each query-document pair
rsvd_scores = {}

for query in queries:
    query_terms = query.split()  # Tokenize the query into terms
    for doc_id, document_text in subproject1.documents.items():
        # Initialize RSVd for the current query-document pair
        rsvd = 0.0

        for term in query_terms:
            # Calculate document frequency for this query using "calculated_doc_frequency"
            df = calculate_doc_frequency(term)

            # Use the "calculate_term_frequency" to return the value for this query (tftd of formula)
            tf = calculate_term_frequency(term, doc_id)

            # Calculate the average document length (Lave)
            Lave = calculate_average_length()

            # I am going to assume we use log of base 10 as it is not indicated in the textbook.
            LHS = math.log10((N - df + 0.5) / (df + 0.5) + 1.0)
            # Calculate the numerator as indicated in formula
            numerator = (k1 + 1.0) * tf
            # Same for denominator as indicated in formula:
            denominator = k1 * ((1 - b) + b * (len(document_text.split()) / Lave)) + tf  # test diff values of k1**
            # Update the RSVd for this query-document pair
            RHS = numerator / denominator

            rsvd += LHS * RHS

        # Store the RSVd score for the current query-document pair
        rsvd_scores[(query, doc_id)] = rsvd

# Simple list of tuples containing query, document, and RSVd scores
ranked_results = [(query, doc_id, rsvd) for (query, doc_id), rsvd in rsvd_scores.items()]


# Simple function to return rsvd result
def sort_RSVd(rsvd_result):
    return rsvd_result[2]  # score is in index location 2, sort by comparing each


# Sort from highest to lowest rank
ranked_results.sort(key=sort_RSVd, reverse=True)

# Print the ranked list of results
for rank, (query, doc_id, rsvd) in enumerate(ranked_results, start=1):
    print(f"Rank {rank}: Query: '{query}', Document {doc_id}: RSVd = {rsvd}")

# tODO
# def query_processor_BM25():
#
#     return result
