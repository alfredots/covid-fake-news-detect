# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 20:09:21 2020

@author: alfredo
"""

import nltk
nltk.download('stopwords')
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix
from nltk.corpus import stopwords
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import urllib3

http = urllib3.PoolManager() # PoolManager
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # Desabilitando avisos
url = "https://raw.githubusercontent.com/roneysco/Fake.br-Corpus/master/full_texts/fake/%d.txt" % 1 # URL da notícia
r = http.request('GET', url) # Copiando notícia
print(r.data.decode('utf-8')) # Print com o texto decodificado

df = pd.DataFrame(columns = ['noticia', 'label'])

print("copiando fake-news")
for i in range(1, 3601):
  url = "https://raw.githubusercontent.com/roneysco/Fake.br-Corpus/master/full_texts/fake/%d.txt" % i # URL da notícia
  r = http.request('GET', url) # Copiando notícia
  noticia = pd.DataFrame([[r.data.decode('utf-8'), 'fake']], columns = ['noticia', 'label'])
  df = df.append(noticia, ignore_index=True)

print("copiando true news")
for i in range(1, 3601):
  url = "https://raw.githubusercontent.com/roneysco/Fake.br-Corpus/master/full_texts/true/%d.txt" % i # URL da notícia
  r = http.request('GET', url) # Copiando notícia
  noticia = pd.DataFrame([[r.data.decode('utf-8'), 'true']], columns = ['noticia', 'label'])
  df = df.append(noticia, ignore_index=True)
  
print("dataframe preparado ")
df.head()

df.to_csv("database-news.csv")