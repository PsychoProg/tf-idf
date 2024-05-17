import nltk


def parse_documents(file_path):
  documents = []
  current_doc = {}
  current_key = None
  doc_id = 0

  with open(file_path, 'r') as f:
    for line in f:
      line = line.strip()

      if line.startswith(".I"):
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
        tokens = nltk.word_tokenize(content)  # Tokenize using NLTK Punkt
        print(tokens)
        current_doc.setdefault(current_key, []).append(tokens)

      elif current_key:
        current_doc.setdefault(current_key, []).append(line.strip())

  if current_doc:
    documents.append(current_doc)

  return documents


# Replace 'your_file.txt' with the actual path to your document file
file_path = "CISI.doc.txt"

# Parse documents and tokenize words
documents = parse_documents(file_path)

# Access the tokenized words in documents dictionary
# For example:
# print(documents[0]["title"][1])  # Access first token of first document's title
# print(documents[1]["content"][2])  # Access third token of first sentence in second document's content
