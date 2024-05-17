import re
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import math
import json 
from collections import Counter
from collections import defaultdict


def parse_documents(file_path):
    documents = []
    current_doc = {}
    doc_id = 0

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()

            if re.match(r'\.I', line):
                if current_doc:
                    documents.append(current_doc)
                current_doc = {}
                doc_id += 1
                current_doc["id"] = doc_id
            elif re.match(r'\.T', line):
                current_doc["content"] = ""
            elif re.match(r'\.A', line):
                pass  # Skip author line
            elif re.match(r'\.W', line):
                pass  # Skip content line
            else:
                current_doc["content"] += line + " "

    if current_doc:
        documents.append(current_doc)

    return documents

# Example Usage
documents = parse_documents("CISI.doc.txt")

"""
print(parsed_documents[0]["content"])

for doc in parsed_documents:
    print(doc)
"""


stop_words = set(stopwords.words('english'))

result_document = []
for doc in documents:
    doc_id = doc["id"]
    # title
    # author
    content = doc["content"]
    content_tokens = [word.lower() for word in word_tokenize(content)]
    filtered_tokens = [w for w in content_tokens if not w.lower() in stop_words]
    clean_text = ' '.join(filtered_tokens)
    # print(clean_text)
    result_document.append(clean_text)

# print(result_document)




def calculate_tf_idf(documents):
    # Step 1: Calculate Term Frequency (TF)
    tf = []
    for doc in documents:
        doc_tf = defaultdict(int)
        words = doc.split()
        word_count = len(words)
        for word in words:
            doc_tf[word] += 1
        tf.append(doc_tf)

    # Step 2: Calculate Inverse Document Frequency (IDF)
    doc_count = len(documents)
    idf = defaultdict(float)
    for doc_tf in tf:
        for word in doc_tf.keys():
            idf[word] += 1

    for word in idf.keys():
        idf[word] = math.log(doc_count / idf[word])

    # Step 3: Calculate TF-IDF
    tf_idf = []
    for i, doc_tf in enumerate(tf):
        doc_tfidf = {}
        for word in doc_tf.keys():
            doc_tfidf[word] = round(doc_tf[word] * idf[word], 4)
        tf_idf.append(doc_tfidf)

    return tf_idf

# Example Usage

result = calculate_tf_idf(result_document)
for i, document in enumerate(result):
    print(f"\nTF-IDF for Document {i + 1}:\n {document}")

