from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn import ensemble
from sklearn.metrics import classification_report, accuracy_score

import pandas as pd
import sqlite3
import regex as re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pickle

def train_model(email):
    df = pd.read_csv('data/emails.csv')
    df=df.drop_duplicates()
    df=df.reset_index(inplace=False)[['text','spam']]

    clean_desc=[]
    for w in range(len(df.text)): 
      desc=df['text'][w].lower()

      #remove punctuation
      desc=re.sub('[^a-zA-Z]',' ', desc)
      #remove tags
      desc=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",desc)

      #remove digits and special chars
      desc=re.sub("(\\d|\\W)+"," ",desc)
    
      clean_desc.append(desc)

    df['text']=clean_desc

    #instantiate the class
    cv=CountVectorizer()

    text_vec=cv.fit_transform(df['text'])

    X_train, X_test, y_train, y_test=train_test_split(text_vec, df['spam'], test_size=0.45, random_state=42, shuffle=True)

    classifier=ensemble.GradientBoostingClassifier(n_estimators=100, 
                                                  learning_rate=0.5,
                                                  max_depth=6
                                                  )
    classifier.fit(X_train, y_train)
    predictions=classifier.predict(X_test)
    '''model_file_path="model/model.pkl"
    pickle.dump(classifier, open(model_file_path, 'wb'))'''
    print(classification_report(y_test, predictions))
    print(type(email))

    test=email.lower()

    #remove punctuation
    test=re.sub('[^a-zA-Z]',' ', test)
    #remove tags
    test=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",test)

    #remove digits and special chars
    test=re.sub("(\\d|\\W)+"," ",test)
    
    new_list=[]
    new_list.append(test)

    test_vectors = cv.transform(new_list)

    if classifier.predict(test_vectors)==1:
      return "This is spam email"
    else:
      return "This is safe email"