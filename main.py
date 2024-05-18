import re
from nltk import word_tokenize
from nltk.corpus import stopwords
import math
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


def parse_query(file_path):
    queries = []
    current_query = {}
    query_id = 0

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()

            if re.match(r'\.I', line):
                if current_query:
                    queries.append(current_query)
                current_query = {}
                query_id += 1
                current_query["id"] = query_id
            elif re.match(r'\.W', line):
                current_query["query"] = ""
            else:
                current_query["query"] += line + " "

    if current_query:
        queries.append(current_query)

    return queries

# Example Usage
documents = parse_documents("mini.CISI.doc.txt")
queries = parse_query("mini.CISI.QRY.txt")

# print(parsed_documents[0]["content"])



stop_words = set(stopwords.words('english')) 

"""
CISI.doc.txt
"""
cisi_document = []
for doc in documents:
    doc_id = doc["id"]
    content = doc["content"]
    content_tokens = [word.lower() for word in word_tokenize(content)]
    filtered_tokens = [w for w in content_tokens if not w.lower() in stop_words]
    clean_text = ' '.join(filtered_tokens)
    # print(clean_text)
    cisi_document.append(clean_text)


"""
CISI.QRY
"""
cisi_query = []
for q in queries:
    q_id = q["id"]
    query = q["query"]
    query_tokens = [word.lower() for word in word_tokenize(query)]
    filtered_tokens = [w for w in query_tokens if not w.lower() in stop_words]
    clean_text = ' '.join(filtered_tokens)
    # print(clean_text)
    cisi_query.append(clean_text)

# print(cisi_query)


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

doc_tf_idf = calculate_tf_idf(cisi_document)
for i, document in enumerate(doc_tf_idf):
    print(f"\nTF-IDF for Document {i + 1}:\n {document}")

print("="*100,"\n","="*100)

q_tf_idf = calculate_tf_idf(cisi_query)
for i, document in enumerate(q_tf_idf):
    print(f"\nTF-IDF for query {i + 1}:\n {document} \t {i}")


"""
=================================
"""

# love = find_best_match(q_tf_idf["query"],doc_tf_idf["content"])
print("documents tf-idf")
print(doc_tf_idf)
print("queries tf-idf")
print(q_tf_idf)


"""
================================
"""

def calculate_cosine_similarity(query_tf_idf, doc_tf_idf):

  numerator = sum(query_tf_idf[word] * doc_tf_idf.get(word, 0) for word in query_tf_idf)
  denominator = math.sqrt(sum(value**2 for value in query_tf_idf.values())) * math.sqrt(sum(value**2 for value in doc_tf_idf.values()))
  return numerator / denominator if denominator > 0 else 0  # Handle division by zero


def find_best_match(query_tf_idf, doc_tf_idfs):
  max_similarity = 0
  best_match_id = None

  for doc_id, doc_tf_idf in enumerate(doc_tf_idfs, start=1):
    cosine_similarity = calculate_cosine_similarity(query_tf_idf, doc_tf_idf)
    if cosine_similarity > max_similarity:
      max_similarity = cosine_similarity
      best_match_id = doc_id

  return {"query_id": 1, "best_match_id": best_match_id}  # Assuming query ID is always 1 (modify if needed)


print("====================================================")
# print(q_tf_idf[0])
print(doc_tf_idf[1])
# best_match = find_best_match(q_tf_idf[0], doc_tf_idf)
# print(f"Query ID: {best_match['query_id']}")
# print(f"Best Matching Document ID: {best_match['best_match_id']}")