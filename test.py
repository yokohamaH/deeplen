from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import matplotlib.pyplot as plt  # 追加
import numpy as np
import random
import sys
import io

path = './debu/aozora/new_ningen_shikkaku.txt'
with io.open(path, encoding='utf-8') as f:
    text = f.read().lower()
#print('corpus length:', len(text))

chars = sorted(list(set(text)))  # 文字の種類

char_indices = dict((c, i) for i, c in enumerate(chars))  # 単語エンコードしたの辞書
indices_char = dict((i, c) for i, c in enumerate(chars))  # キーと要素が逆になっている

# print(char_indices)
# print(indices_char)
# cut the text in semi-redundant sequences of maxlen characters
maxlen = 8  # 1センテンス当たりの文字数
step = 1  # センテンスのずらす大きさ
sentences = []
next_chars = []

for i in range(0, len(text) - maxlen, step):
    # 8文字でひたすら1文字ずつずらしたのをlistに入れる　実際の学習データの単位
    sentences.append(text[i: i + maxlen])
    next_chars.append(text[i + maxlen])  # 1文字づつわけるだけ ただし8個スタートは8文字目から

x = np.zeros((len(sentences), maxlen, len(chars)),
             dtype=np.bool)  # len(sentences)*8*len(chars)の要素全部Falseのテンソル
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)

for i, sentence in enumerate(sentences):
    print(i)
    for t, char in enumerate(sentence):
        # one-hotエンコーディングそれぞれのセンテンスで使われている単語のインデックスの部分がTRUEに
        x[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1
# xはそれぞれのセンテンスに使われている文字一覧と1文字１文字の情報を含んでいてyはセンテンスとそれに使われている文字のみ
# さらにyはxのセンテンスの次の8個のセンテンスが対応している　教師ラベルは次のセンテンス
