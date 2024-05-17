import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords


def parse_documents(file_path):
  documents = []
  current_doc = {}
  current_key = None
  doc_id = 0

  with open(file_path, 'r') as f:
    for line in f:
      line = line.strip()

      if line.startswith(".I"):
        # New document
        if current_doc:
          documents.append(current_doc)
        current_doc = {}
        doc_id += 1
        current_key = "id"
        current_doc["id"] = doc_id

      elif line.startswith(".T"):
        current_key = "title"
        current_doc.setdefault(current_key, []).append(line.strip())  # Handle multi-line titles

      elif line.startswith(".A"):
        current_key = "author"

      elif line.startswith(".W"):
        current_key = "content"
        content = line.lower()
        tokens = word_tokenize(content)  # Tokenize using NLTK Punkt
        stop_words = set(stopwords.words('english'))
        filtered_sentence = [w for w in tokens if not w.lower() in stop_words]
        current_doc["filtered_content"] = filtered_sentence  # Store filtered tokens

      elif current_key:
        # Append content to existing key
        current_doc.setdefault(current_key, []).append(line.strip())

  # Add the last document
  if current_doc:
    documents.append(current_doc)

  return documents


# Set your file path
file_path = "CISI.doc.txt"

# Parse the documents
documents = parse_documents(file_path)

# Create a new list to store filtered sentences
res_list = []

# Extract filtered sentences from each document and store them in res_list
for doc in documents:
  res_list.extend(doc.get("filtered_content", []))

# Print the list of filtered sentences (optional)
print(res_list)
