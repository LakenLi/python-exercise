#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: horan
"""
import time
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
 
print("start.............")
time_start = time.time()
 
df_train = pd.read_csv('./train_set.csv')
df_test = pd.read_csv('./test_set.csv')
 
df_train.drop(columns = ['article','id'], inplace = True)
df_test.drop(columns = ['article'], inplace = True)
 
vectorizer = TfidfVectorizer()
x_train = vectorizer.fit_transform(df_train['word_seg'])
x_test = vectorizer.transform(df_test['word_seg'])
y_train = df_train['class']-1
 
classifier = LogisticRegression()
classifier.fit(x_train,y_train)
 
y_test = classifier.predict(x_test)
 
df_test['class'] = y_test.tolist()
df_test['class'] = df_test['class'] + 1
df_result = df_test.loc[:,['id','class']]
df_result.to_csv('./result3.csv',index=False)
 
time_end = time.time()
print(time_end - time_start)
 
print("ended............")