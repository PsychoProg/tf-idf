import math
from collections import defaultdict

def calculate_cosine_similarity(query_tf_idf, doc_tf_idf):

  numerator = sum(query_tf_idf[word] * doc_tf_idf.get(word, 0) for word in query_tf_idf)
  denominator = math.sqrt(sum(value**2 for value in query_tf_idf.values())) * math.sqrt(sum(value**2 for value in doc_tf_idf.values()))
  return numerator / denominator if denominator > 0 else 0  # Handle division by zero


def find_best_match(query_tf_idf, doc_tf_idfs):
  """
  Finds the document ID with the highest cosine similarity to the query.

  Args:
      query_tf_idf: A dictionary containing TF-IDF values for the query.
      doc_tf_idfs: A list of dictionaries, where each dictionary contains TF-IDF values for a document.

  Returns:
      A dictionary containing "query_id" and "best_match_id" keys.
  """
  max_similarity = 0
  best_match_id = None

  for doc_id, doc_tf_idf in enumerate(doc_tf_idfs, start=1):
    cosine_similarity = calculate_cosine_similarity(query_tf_idf, doc_tf_idf)
    if cosine_similarity > max_similarity:
      max_similarity = cosine_similarity
      best_match_id = doc_id

  return {"query_id": 1, "best_match_id": best_match_id}  # Assuming query ID is always 1 (modify if needed)


query_tf_idf = {'word1': 0.5, 'word2': 0.3}  # Example query TF-IDF
doc_tf_idfs = [
    {'word1': 0.2, 'word2': 0.8},  # Example document 1 TF-IDF
    {'word3': 0.4, 'word4': 0.6},  # Example document 2 TF-IDF
]

best_match = find_best_match(query_tf_idf, doc_tf_idfs)
print(f"Query ID: {best_match['query_id']}")
print(f"Best Matching Document ID: {best_match['best_match_id']}")
