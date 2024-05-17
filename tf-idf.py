import math
from collections import defaultdict

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
            doc_tfidf[word] = doc_tf[word] * idf[word]
        tf_idf.append(doc_tfidf)

    return tf_idf

# Example Usage
documents = ['present study history dewey decimal classification . first edition ddc published', 'report analysis 6300 acts use 104 technical libraries united kingdom .']
result = calculate_tf_idf(documents)
for i, document in enumerate(result):
    print(f"TF-IDF for Document {i + 1}: {document}")