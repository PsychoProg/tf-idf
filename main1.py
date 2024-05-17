# Assuming you've saved the code in a Python file (e.g., parse_documents.py)
import parse_documents  # Replace with your actual file name

# Set your file path
file_path = "CISI.doc.txt"

# Parse the documents
# documents = parse_documents.parse_documents(file_path)

# Access first document data

# first_doc_id = documents[0]["id"]
# first_doc_title = documents[0]["title"]
# first_doc_content = " ".join(documents[0]["content"])  # Join content lines
# first_doc_id = documents[0]["id"]

# print(f"First Document id: {first_doc_id}")
# print(f"First Document id:\t {first_doc_id}")
# print(f"First Document title:\n {first_doc_title}")
# print(f"First Document Content:\n{first_doc_content}")
# print(documents[0])


""" ================================= """
from collections import Counter
import math


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
        current_doc.setdefault(current_key, []).append(line.strip())  # Handle multi-line content

      elif current_key:
        current_doc.setdefault(current_key, []).append(line.strip())

  if current_doc:
    documents.append(current_doc)

  return documents


def calculate_tf_idf(documents):
  global_word_counts = Counter()

  for doc in documents:
    content = doc.get("title", []) + doc.get("content", [])
    for line in content:
      global_word_counts.update(line.lower().split())

  total_documents = len(documents)

  for doc in documents:
    term_frequencies = {}
    inverse_document_frequencies = {}

    content = doc.get("title", []) + doc.get("content", [])
    for line in content:
      for word in line.lower().split():
        term_frequencies[word] = term_frequencies.get(word, 0) + 1

    for term, count in term_frequencies.items():
      term_frequencies[term] /= len(content)
      inverse_document_frequencies[term] = math.log(total_documents / (global_word_counts[term] + 1))

    doc["tf"] = term_frequencies
    doc["idf"] = inverse_document_frequencies


def save_tf_idf_to_file(documents):
  with open("result.txt", "w") as f:
    for doc in documents:
      f.write(f"Document ID: {doc['id']}\n")
      f.write(f"Term Frequencies (TF):\n")
      for term, tf in doc["tf"].items():
        f.write(f"{term}: {tf}\n")
      f.write(f"Inverse Document Frequencies (IDF):\n")
      for term, idf in doc["idf"].items():
        f.write(f"{term}: {idf}\n")
      f.write("=" * 50 + "\n")  # Separator line


# Replace 'your_file.txt' with the actual path to your document file
file_path = "CISI.doc.txt"

# Parse documents
documents = parse_documents(file_path)

# Calculate TF-IDF
calculate_tf_idf(documents)

# Save results to file
save_tf_idf_to_file(documents)
