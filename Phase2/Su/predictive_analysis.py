# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 01:22:47 2016

@author: hillarysu
"""
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
from patsy import dmatrices
from sklearn.linear_model import LogisticRegression

dataFile = open('dataChicagoCrime2.csv','r')
dataChicagoCrime = pd.read_csv(dataFile, sep=',', encoding='latin1')

dataFile = open('dataMontgomeryCrime.csv','r')
dataMontgomeryCrime = pd.read_csv(dataFile, sep=',', encoding='latin1')


'''t-test'''
def Hour(x):
    h, m, s = x.split(':')
    t = int(h) + int(m)/60 + int(s)/360
    return t
dataChicagoCrime['time_hour'] = dataChicagoCrime['time'].apply(Hour)
dataMontgomeryCrime['time_hour'] = dataChicagoCrime['time'].apply(Hour)

print(dataChicagoCrime['time_hour'].mean())
print(dataMontgomeryCrime['time_hour'].mean())

t_test = stats.ttest_ind(a= dataMontgomeryCrime['time_hour'],b= dataMontgomeryCrime['time_hour'],equal_var=False)
print(t_test)
print()



'''Logistical Regression'''

# construct new dataframe which has attributes 
#'community_area','primary_type','weekdayNum','time_section'
# 'weekdayNum': 1 represents Monday, 2 represents Tuseday, ...
# 'time_section' : 1 represents 0:00-4:00, 2 represents 4:00-8:00, ...
myDataFrame = pd.concat([dataChicagoCrime['community_area'], dataChicagoCrime['primary_type'],dataChicagoCrime['weekdayNum'],dataChicagoCrime['time_section']], axis=1)

# add "affair" column: 1 represents having affairs, 0 represents not
myDataFrame['affair'] = (myDataFrame.primary_type == 'THEFT').astype(int)
pprint(myDataFrame.head())
print()

# create dataframes with an intercept column and dummy variables for time_section
y, X = dmatrices('affair ~ community_area + weekdayNum + C(time_section) ', myDataFrame, return_type="dataframe")
#print(X.columns)
#print()

# flatten y into a 1-D array
y = np.ravel(y)

# instantiate a logistic regression model, and fit with X and y
model = LogisticRegression()
model = model.fit(X, y)

#predicting the probability of a theft crime which happens in community 23 in 12:00-16:00 on Friday
#[1, 0, 0, 1, 0, 0, 23 ,5]
#[Intercept, time_section_2, time_section_3, time_section_4, time_section_5, time_section_6, community_area, weekdayNum]
#The order of parameters is same as the order of X.columns

predict_prob = model.predict_proba(np.array([1, 0, 0, 1, 0, 0, 23 ,5]))
print('the probability of a theft crime happens in community 23 in 12:00-16:00 on Friday:')
print(predict_prob[0][1])
print()


