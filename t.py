from collections import Counter
import math

# Given list of documents
documents = [
  'Geeks for geeks',
  'Geeks',
  'r2j',
]



# Calculate TF for each document
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
tf_values = [calculate_tf(document) for document in documents]

# Calculate IDF for all documents
idf_values = calculate_idf(documents)

# Print TF and IDF values
for i, document in enumerate(documents):
    print(f"TF values for Document {i+1}: {tf_values[i]}")
    
print("\nIDF values:")
for word, idf in idf_values.items():
    print(f"{word}: {idf}")