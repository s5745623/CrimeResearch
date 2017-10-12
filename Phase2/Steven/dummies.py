#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 23:27:52 2016

@author: yuanyaozhang
"""

from pprint import pprint
import pandas as pd

from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import cross_validation
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC



dataFile = open('dataMontgomeryCrime.csv','r')
dataMontgomeryCrime = pd.read_csv(dataFile, sep=',', encoding='latin1')

dataMontgomeryCrime_C = pd.get_dummies(dataMontgomeryCrime['city'])



dataMontgomeryCrime_T = pd.get_dummies(dataMontgomeryCrime['time_section'])
dataMontgomeryCrime1 = dataMontgomeryCrime_C.join(dataMontgomeryCrime_T)

valueArray = dataMontgomeryCrime1.values

X = valueArray[:,0:47]
Y = valueArray[:,48]
test_size = 0.20
seed = 7
X_train, X_validate, Y_train, Y_validate = cross_validation.train_test_split(X, Y, test_size=test_size, random_state=seed)


num_folds = 10
num_instances = len(X_train)
seed = 7
scoring = 'accuracy' 

models = []
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
#models.append(('NB', GaussianNB()))
#models.append(('SVM', SVC()))

results = []
names = []
for name, model in models:
	kfold = cross_validation.KFold(n=num_instances, n_folds=num_folds, random_state=seed)
	cv_results = cross_validation.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)
########then set the range of X Y  