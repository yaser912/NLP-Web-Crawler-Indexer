# Yaser Aleem - 40017879
# Project 3 - Refined indexing + implementation of ranking returned terms
import tarfile, os, time
from bs4 import BeautifulSoup
from pathlib import Path
from nltk import word_tokenize

# step 1
# extract files from zip file reuters 21578

tar_file_path = "reuters21578.tar.gz"
extract_to = 'Reuters Doc'  # extract the first news doc to this folder.


def extract_files(tar_file_source, destination):
    with tarfile.open(tar_file_source, 'r') as tar:
        for member in tar.getmembers():
            if ".sgm" in member.name:  # news articles end in sgm for html
                tar.extract(member, path=destination)


extract_files(tar_file_path, extract_to)


def extract_data(files):
    path = Path(os.getcwd() + "\\documents")
    path.mkdir(exist_ok=True)
    os.chdir(path)  # change directory to initial output. write files to that directory.
    postingsList = {}  # initialize empty postings list dictionary
    count = 1
    # loop thru files in the Reuters Doc folder.
    for file in files:
        f = open(file)
        raw = f.read()
        soup = BeautifulSoup(raw, "html.parser")
        id = soup.find_all("reuters")
        size = len(id)
        articles = {}
        for document in range(size):
            articleText = id[document].text.replace("\n", " ")
            articles[id[document].get("newid")] = articleText
            tokens = [word for word in word_tokenize(id[document].text) if word.isalpha()]
            unique_terms = set(tokens)
            for term in unique_terms:
                # if count == 10000:
                #     return postingsList, articles  # remove this for all postings.
                if term in postingsList:
                    postingsList[term].append(count)
                else:
                    postingsList[term] = [count]
            count += 1
    return postingsList, articles


dir = os.getcwd() + "\\Reuters Doc"  # grab files from this folder
files = Path(dir).glob('*')  # asterisk to get all files in directory
documents = {}
start_time = time.time()
postlist, documents = extract_data(files)
end_time = time.time()
elapsed_time = end_time - start_time

# part a
# print(f"SPIMI procedure took {elapsed_time:.2f} seconds to complete.")


# part b
invertedIndex = {}
for term, doc_id in postlist.items():
    invertedIndex[term] = doc_id


# process a query with 1 or more terms using AND
def query_processor(inverted_index):
    query = input("Enter one or more keywords separated by spaces: ")
    # seperate the key words using split()
    keywords = query.split()  # this is now a list that contains the information needs we are interested in

    matching_docs = []  # initialize an empty list which will hold all documents that intersect.
    for keyword in keywords:
        if keyword in inverted_index:  #
            doc_ids = inverted_index[keyword]
            if not matching_docs:
                matching_docs = doc_ids
            else:
                # Perform an AND operation by keeping only the common doc_ids
                matching_docs = list(set(matching_docs) & set(doc_ids))
        else:
            # If a keyword is not found, exit the loop early
            print(f"'{keyword}' not found in the documents.")
            matching_docs = []
            break

    if matching_docs:
        print(f"Documents containing all keywords: {matching_docs}")
    else:
        print("No documents found.")


# Invoke the query processor
query_processor(invertedIndex)
