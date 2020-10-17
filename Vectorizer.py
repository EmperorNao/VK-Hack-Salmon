from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import DictVectorizer
import pandas as pd
import numpy as np
import scipy

# get texts from bd
f = open("for_vladuk.txt", encoding='utf-8')
line = f.readlines()

d = {'text':line}
texts = pd.DataFrame(d)
texts.text = texts.text.replace('[^а-яА-Я0-9]', ' ', regex = True).str.lower()

for i in range(0, len(texts.text)):

    t_str = ""
    for word in texts.text[i].split(' '):

        if len(word) != 1:

            t_str += word + " "

    texts.text[i] = t_str


vectorizer = TfidfVectorizer()
words_train = vectorizer.fit_transform(texts.text) #тупая матрица с циферками
words = vectorizer.get_feature_names()
words_train_densed = words_train.todense() # матрица
enc = DictVectorizer()
n = 10


for row in words_train_densed:


    row = np.array(row)
    indices = (-row).argsort()[:n]
    indices = indices[0][:n]


    most_values_words = [words[i] for i in indices]
    print(most_values_words)






'''
arr_sq={}
for i in range(0,len(texts.text)):
    seq = texts.text[i].split()
    for j in range(0, len(seq)):

        arr_sq[seq[j]] = numbers[i,j]


arr_keys = []
arr_values = []
for key in arr_sq.keys():

    arr_keys.append(key)
    arr_values.append(arr_sq[key])

n = 10
arr_values = np.reshape(arr_values, -1)
print(arr_values)
print(arr_keys)
indices = (-arr_values).argsort()[:n]

most_values_words = [arr_keys[i] for i in indices]

print(most_values_words)

# print(words_test)

'''