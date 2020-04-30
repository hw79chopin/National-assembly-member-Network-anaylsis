import numpy as np
import pandas as pd
from collections import Counter
import konlpy
from konlpy.tag import Mecab
from sklearn.manifold import TSNE
import fasttext
from gensim.models import Word2Vec, FastText
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity

embedding_model = Word2Vec(corpus, size=100, window = 2, min_count=10, workers=4, iter=100, sg=1)

embedding_model.most_similar(positive=['착취'], topn=10)


# dictionary 형태로 단어와 벡터 묶기
word_dict = {}
for vocab, vector in zip(embedding_model.wv.index2word, matrix):
    word_dict[vocab] = vector

cosine_similarity(word_dict['성폭력'].reshape(1,-1), word_dict['성범죄'].reshape(1,-1))
# 이렇게 하면 wv.most_similar('성푝력') 유사도와 똑같이 나온다.

embedding_model['성폭력'] # 이렇게 vector를 불러올 수도 있음!!