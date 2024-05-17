import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import math
import json 
from collections import Counter


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

# print(mylist)

# with open("fruits.txt", "w") as f:
#   f.write(str(mylist))


def calculate_tf(document):
    tf_dict = {}
    # Tokenize the document by splitting on spaces
    words = document.lower().split()
    # === must test 
    word_count = len(words)
    
    word_freq = Counter(words)
    # === must test 
    
    for word in word_freq:
        tf_dict[word] = word_freq[word] / word_count
    return tf_dict

# Calculate IDF for all documents
def calculate_idf(documents):
    N = len(documents)
    unique_words = set()
    
    for document in documents:
        unique_words.update(set(document.lower().split()))
    
    idf_dict = {}
    
    for word in unique_words:
        word_count = sum(1 for document in documents if word in document.lower())
        idf_dict[word] = math.log10(N / word_count)
        
    return idf_dict

# Calculate TF for each document
tf_values = [calculate_tf(document) for document in result_document]

# Calculate IDF for all documents
idf_values = calculate_idf(result_document)

# Print TF and IDF values
res_list = []
for i, document in enumerate(result_document):
    print(f"TF values for Document {i+1}: {tf_values[i]}")
    
print("\nIDF values:")
for word, idf in idf_values.items():
    print(f"{word}: {idf}")