from __future__ import print_function
from keras.callbacks import LambdaCallback
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np
import random
import pickle

f = open("./chars.txt", "rb")  # list型としてload
chars = pickle.load(f)
f.close()
f = open("re2_ningen_shikkaku.txt", "rb")  # list型としてload
text = pickle.load(f)
f.close()

char_indices = dict((c, i) for i, c in enumerate(chars))  # 単語エンコードしたの辞書
indices_char = dict((i, c) for i, c in enumerate(chars))  # キーと要素が逆になっている

maxlen = 8
step = 1
sentences = []
next_chars = []

for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i + maxlen])  # 8文字でひたすら1文字ずつずらしたのをlistに入れる
    next_chars.append(text[i + maxlen])  # 1文字づつわけるだけ

x = np.zeros((len(sentences), maxlen, len(chars)),
             dtype=np.bool)  # len(sentences)*8*len(chars)の要素全部Falseのテンソル
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)


for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        x[i, t, char] = 1  # one-hotエンコーディングそれぞれのセンテンスで使われている単語のインデックスの部分がTRUEに
    y[i, next_chars[i]] = 1

    # xはそれぞれのセンテンスに使われている文字一覧と1文字１文字の情報を含んでいてyはセンテンスとそれに使われている文字のみ
print(x)
