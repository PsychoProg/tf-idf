import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

 
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

# Access first document data

first_doc_id = documents[0]["id"]
first_doc_title = documents[0]["title"]


first_doc_content = " ".join(documents[0]["content"])  # Join content lines

# print(len(documents))

# print(f"First Document id:\n {first_doc_id}")
# print(f"First Document title:\n {first_doc_title}")
# print(f"First Document Content:\n{first_doc_content}")
# print(documents[0])

stop_words = set(stopwords.words('english'))

def process_documents(documents):
  processed_documents = []
  for doc in documents:
    doc_id = doc["id"]
    content = doc.get("content", [])  # Handle documents with no title
    content_tokens = [word.lower() for word in word_tokenize(" ".join(content))]  # Tokenize and lowercase title
    filtered_sentence = [w for w in content_tokens if not w.lower() in stop_words]
    processed_documents.append({"id": doc_id, "content_tokens": filtered_sentence})
  return processed_documents


# Process documents and get the new list
processed_documents = process_documents(documents)

# Print the processed document list (optional)
print(processed_documents)
