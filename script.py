import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import math
import json 
from collections import Counter
from collections import defaultdict


# nltk.download('stopwords')
# print(stopwords.words('english'))

def parse_documents(file_path):
  documents = []
  current_doc = {}
  current_key = None
  doc_id = 0  # Initialize document ID counter

  with open(file_path, 'r') as f:
    for line in f:
      line = line.strip()  # Remove leading/trailing whitespace

      if line.startswith(".I"):
        # New document
        if current_doc:
          documents.append(current_doc)
        current_doc = {}
        doc_id += 1  # Increment document ID counter
        current_key = "id"
        current_doc["id"] = doc_id  # Assign ID to document
      elif line.startswith(".T"):
        current_key = "title"
      elif line.startswith(".A"):
        current_key = "author"
      elif line.startswith(".W"):
        current_key = "content"
      elif current_key:
        # Append content to existing key
        current_doc.setdefault(current_key, []).append(line.strip())  # Handle multi-line content

  # Add the last document
  if current_doc:
    documents.append(current_doc)

  return documents



# Set your file path
file_path = "mini.CISI.doc.txt"

# Parse the documents
documents = parse_documents(file_path)
# print(documents)
# print(type(documents))
# Access first document data

# first_doc_id = documents[0]["id"]
# first_doc_title = documents[0]["title"]
# first_doc_content = " ".join(documents[0]["content"])  # Join content lines


stop_words = set(stopwords.words('english'))

result_document = []
for doc in documents:
  doc_id = doc["id"]
  # title
  # author
  content = doc["content"]
  content_tokens = [word.lower() for word in word_tokenize(" ".join(content))]
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
            doc_tfidf[word] = doc_tf[word] * idf[word]
        tf_idf.append(doc_tfidf)

    return tf_idf

# Example Usage
result = calculate_tf_idf(result_document)
for i, document in enumerate(result):
    print(f"TF-IDF for Document {i + 1}: {document}")

# with open("fruits.txt", "w") as f:
#   f.write(str(mylist))


