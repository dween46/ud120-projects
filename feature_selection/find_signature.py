#!/usr/bin/python

import pickle
import numpy as np
np.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "word_data_overfit_unix.pkl"
authors_file = "email_authors_overfit_unix.pkl"
word_data = pickle.load( open(words_file, "rb"))
authors = pickle.load( open(authors_file, "rb"))



### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()


### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]



### your code goes here
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)


print(accuracy_score(labels_test, pred))
#print("importance: ", [item for item in clf.feature_importances_ if item > 0.2 ])
#index = np.where(clf.feature_importances_ > 0.2)[0][0]
#print("index of the word: ", index)
#print("problem word: ", vectorizer.get_feature_names()[index])

problemWordIndices = []

importances = clf.feature_importances_
for index in range(len(importances)):
    if importances[index] > 0.2:
        print ("index:", index)
        problemWordIndices.append(index)
        print ("importance:", importances[index])

for index in problemWordIndices:
    print ("problem word:", vectorizer.get_feature_names()[index])
    







