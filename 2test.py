from collections import Counter
import math

def calculate_tf_idf(documents):
  word_counts = Counter()  # Count word occurrences across all documents
  for doc in documents:
    word_counts.update(doc.lower().split())  # Tokenize and lowercase words

  total_documents = len(documents)  # Number of documents
  tf_idf = {}
  for word, count in word_counts.items():
    tf = count / len(word_counts)  # Calculate TF (term frequency)
    df = count  # Document frequency within the list (estimated)
    estimated_idf = 1.0 + math.log(total_documents / (df + 1))  # Estimated IDF (using log1p for smoothing)
    tf_idf[word] = {'tf': "{:.2f}".format(tf), 'idf': "{:.2f}".format(estimated_idf)}
  return tf_idf

# Your list of documents
documents = [
  'This is the first document.',
  'This document is the second document.',
  'And this is the third one.',
  'Is this the first document?',
  'Is this the second cow?, why is it blue?',
]

# Calculate TF-IDF
tf_idf = calculate_tf_idf(documents)

# Print the TF-IDF dictionary
print(tf_idf)
