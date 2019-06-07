from janome.tokenizer import Tokenizer
from gensim.models import word2vec
import re

binary_data = open(
    './debu/prepro_aozora/data_rojinto_dazai.txt', 'rb').read()
text = binary_data.decode('shift_jis')
print(text)
