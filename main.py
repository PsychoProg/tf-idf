import nltk
from collections import Counter
import math

# Download NLTK Punkt tokenizer and stopwords for your language (replace 'english' if needed)
nltk.download('punkt')
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')


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
        filtered_tokens = [word for word in tokens if word not in stopwords]  # Remove stopwords
        current_doc.setdefault(current_key, []).append(filtered_tokens)

      elif current_key:
        current_doc.setdefault(current_key, []).append(line.strip())

  if current_doc:
    documents.append(current_doc)

  return documents


def calculate_tf_idf(documents):
  global_word_counts = Counter()
  term_document_frequencies = Counter()

  for doc in documents:
    content = doc.get("title", []) + doc.get("content", [])
    for line in content:
      for word in line:
        global_word_counts[word] += 1
        term_document_frequencies[word] += 1  # Track word occurrence per document

  total_documents = len(documents)

  for doc in documents:
    term_frequencies = {}
    inverse_document_frequencies = {}

    unique_words = set(word for line in doc.get("title", []) + doc.get("content", []) for word in line)

    for word in unique_words:
      term_frequencies[word] = term_document_frequencies[word] / len(doc.get("title", []) + doc.get("content", []))
      inverse_document_frequencies[word] = math.log(total_documents / (global_word_counts[word] + 1))

    doc["tf"] = term_frequencies
    doc["idf"] = inverse_document_frequencies


def save_tf_idf_to_file(documents):
  with open("result.txt", "w") as f:
    for doc in documents:
      f.write(f"Document ID: {doc['id']}\n")
      f.write(f"Term Frequencies (TF) - Unique Words:\n")
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
