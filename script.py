from itertools import islice
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
import matplotlib.pyplot as plt

"""
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('stopwords')
"""

def load_doc(filename):
    my_text = list()
    with open(filename, encoding= "utf-8") as f:
        for line in islice(f, 0, None):
            my_text.append(line)
            
    my_text = [word_tokenize(sentence) for sentence in my_text]
    flat_list = [item for sublist in my_text for item in sublist]
    # print(len(flat_list)) # 463455
    return flat_list


def prepare_text(list_of_words):
  #load stopwords:
  stops = stopwords.words('english')
  #transform all word characters to lower case:
  list_of_words = [word.lower() for word in list_of_words]
  #remove all words containing up to two characters:
  list_of_words = [word for word in list_of_words if len(word)>2]
  #remove stopwords:
  list_of_words = [word for word in list_of_words if word not in stops]
  
#   print(list_of_words)
#   print("\n","*"*100,"\n")
#   print(len(list_of_words)) # 257693
  
  return list_of_words


def count_freq(my_list):
    unique_words = []
    counts = []
    # create a list of unique words:
    for item in my_list:
      if item not in unique_words: 
        unique_words.append(item)
    # count the frequency of each word:
    for word in unique_words:
      count = 0
      for i in my_list:
        if word == i:
          count += 1
      counts.append(count)
      
    df = pd.DataFrame({"word": unique_words, "count": counts})
    df.sort_values(by="count", inplace = True, ascending = False)
    df.reset_index(drop=True, inplace = True)
    return df


# FILENAME = "./CISI.ALL.txt"
FILENAME = "modified_file.txt"

cisi_text = load_doc(FILENAME)
prepare_cisi = prepare_text(cisi_text)
cisi_df = count_freq(prepare_cisi)


cisi_df["TF"] = cisi_df["count"]/sum(cisi_df["count"])
print(cisi_df["TF"])


#left join all dataframes:
# thacher_otis = thacher_df[["word", "TF"]].merge(
#     otis_df[["word", "TF"]], 
#     on = "word", 
#     how = "outer", 
#     suffixes = ("_thacher", "_otis")).fillna(0)


