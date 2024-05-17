import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))


def process_documents(documents):
  processed_documents = []
  for doc in documents:
    doc_id = doc["id"]
    title = doc.get("title", [])  # Handle documents with no title
    title_tokens = [word.lower() for word in word_tokenize(" ".join(title))]  # Tokenize and lowercase title
    filtered_sentence = [w for w in title_tokens if not w.lower() in stop_words]
    processed_documents.append({"id": doc_id, "title_tokens": filtered_sentence})
  return processed_documents

# Your existing list of documents (replace with your actual list)
documents = [
  {'id': 1, 'title': ['18 Editions of the Dewey Decimal Classifications'], 'author': ['Comaromi, J.P.'], 'content': [...]},
  {'id': 2, 'title': ['Use Made of Technical Libraries'], 'author': ['Slater, M.'], 'content': [...]},
]

# Process documents and get the new list
# processed_documents = process_documents(documents)

# Print the processed document list (optional)
# print(processed_documents)

""" ======================================= """




def calculate_tf(documents):
  processed_documents = []
  for doc in documents:
    doc_id = doc["id"]
    title_tokens = doc["title_tokens"]
    tf = {}
    for token in title_tokens:
      tf[token] = tf.get(token, 0) + 1  # Count term frequency
    total_terms = len(title_tokens)
    for token, count in tf.items():
      tf[token] = count / total_terms  # Calculate TF
    processed_documents.append({"id": doc_id, "tf": tf})
  return processed_documents

# Your existing list of documents
documents = [
  {'id': 1, 'title_tokens': ['18', 'editions', 'dewey', 'decimal', 'classifications']},
  {'id': 2, 'title_tokens': ['use', 'made', 'technical', 'libraries']},
]

# Calculate TF and get the processed list
processed_documents = calculate_tf(documents)

# Print the processed document list (optional)
print(processed_documents)

