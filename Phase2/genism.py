#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 23:27:52 2016

@author: yuanyaozhang
"""
from gensim import corpora
from collections import defaultdict
from pprint import pprint
import pandas as pd

documents = open('dataMontgomeryCrime.csv','r')
#documents = pd.read_csv(dataFile, sep=',', encoding='latin1')

#remove common words and tokenize
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
          for document in documents]
          
# remove words that appear only once

frequency = defaultdict(int)
for text in texts:
    for token in text:
         frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1]
         for text in texts]

  # pretty-printer
pprint(texts)