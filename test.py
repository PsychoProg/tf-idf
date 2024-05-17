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
processed_documents = process_documents(documents)

# Print the processed document list (optional)
print(processed_documents)
