from pathlib import Path
import glob
import numpy as np
import pandas as pd
import num2words
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
df = pd.read_pickle('Files/new_df')

text_titles = ['B00HWEMZ1E',
 'B00I2KY5TM',
 'B00IZ1X21K',
 'B00JEHJMG8',
 'B00JH2WF0K',
 'B00JH2WPO6',
 'B00JS73V2U',
 'B00JYR6GGM',
 'B00K0NS0P4',
 'B00KM10ITK',
 'B00LAEA84S',
 'B00LIYEMTC',
 'B00MWI4HW0',
 'B00MWI4KKE',
 'B00N532A34',
 'B00N532DU4',
 'B00NKR9MJA',
 'B00NKRE7MW']
def preprocessing(text):
    # split into tokens
    tokens = word_tokenize(text)
    # convert to lower case
    tokens = [w.lower() for w in tokens]
    # remove punctuation from each word
    import string
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]

    # convert number and remove tokens that are not alphabetic
    words = []
    for word in stripped:
        if word.isdigit():
            words.append(num2words.num2words(word))
        elif word.isalpha():
            words.append(word)

    # remove stop words and single characters
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words and len(w) > 1]

    # stemming and lemmatization
    porter = PorterStemmer()
    words = [porter.stem(word) for word in words]
    doc = ' '.join(words)
    doc = doc.translate(str.maketrans('', '', string.punctuation))
    return doc


tfidf_vectorizer = TfidfVectorizer()
filenames1 = []


def process(text):
    Search1 = text
    docs1 = []
    docs1.append(preprocessing(Search1))
    tfidf_vector1 = tfidf_vectorizer.fit_transform(docs1)
    tfidf_df1 = pd.DataFrame(tfidf_vector1.toarray(), columns=tfidf_vectorizer.get_feature_names())
    frames = [df, tfidf_df1]
    result = pd.concat(frames)
    k = result.replace(np.nan, 0)
    Sim1 = cosine_similarity(k)
    Sim_s1 = Sim1[-2][:-2]
    top10_s1 = np.argsort(Sim_s1)[-5:]

    for item in top10_s1:
        filenames1.append(text_titles[item])
    return filenames1
