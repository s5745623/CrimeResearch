# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 01:22:47 2016

@author: hillarysu
"""
import pandas as pd
from scipy import stats
import numpy as np
from pprint import pprint
from sklearn.metrics import roc_curve
from sklearn.cross_validation import cross_val_score
#from sklearn.metrics import confusion_matrix
from pandas_ml import ConfusionMatrix
from matplotlib import pyplot as plt
from patsy import dmatrices
from sklearn.linear_model import LogisticRegression
from sklearn import tree 
from sklearn import cross_validation 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

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
dataMontgomeryCrime['time_hour'] = dataMontgomeryCrime['time'].apply(Hour)


'''Hypothesis 1'''
print('-------Hypothesis 1 test-------')
'''Logistical Regression'''
# construct new dataframe which has attributes 
#'community_area','primary_type','weekdayNum','time_section'
# 'weekdayNum': 1 represents Monday, 2 represents Tuseday, ...
# 'time_section' : 1 represents 0:00-4:00, 2 represents 4:00-8:00, ...

myDataFrame = pd.concat([dataChicagoCrime['community_area'],dataChicagoCrime['weekdayNum'],dataChicagoCrime['time_section'], dataChicagoCrime['primary_type']], axis=1)
myDataFrame = myDataFrame.dropna()
# add "affair" column: 1 represents having affairs, 0 represents not
myDataFrame['affair'] = (myDataFrame.primary_type == 'THEFT').astype(int)

# create dataframes with an intercept column and dummy variables for time_section
y, X = dmatrices('affair ~ community_area + weekdayNum + C(time_section) ', myDataFrame, return_type="dataframe")

# flatten y into a 1-D array
y = np.ravel(y)

# instantiate a logistic regression model, and fit with X and y
model = LogisticRegression()
model = model.fit(X, y)

#predicting the probability of a theft crime which happens in community 23 in 12:00-16:00 on Friday
#[1, 0, 0, 1, 0, 0, 23 ,5]
#[Intercept, time_section_2, time_section_3, time_section_4, time_section_5, time_section_6, community_area, weekdayNum]
#The order of parameters is same as the order of X.columns
predict_prob = model.predict_proba(np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 23 ,5]))
print('Logistical Regression')
print('On Friday, the probability of a theft crime happens in community 23 from 18:00pm to 20:00pm in Chicago is')
print(predict_prob[0][1])
print()
print()


'''Decisiton tree'''
print('Decisiton tree')
features = list(myDataFrame.columns[:3])
X = myDataFrame[features]
y = myDataFrame['affair']

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.4,random_state=0)
                                                                     
clf = tree.DecisionTreeClassifier()  
clf = clf.fit(X_train, y_train)

#cross-validation                                                                       
score = cross_val_score(clf, X_test, y_test, cv=10)
print('cross-validation score:',score)

#ROC cirve
test_predictions = clf.predict_proba(X_test)
fpr, tpr,thresholds = roc_curve(y_test,test_predictions[:,1:2])
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC curve')
plt.show()
print()

#confusion matrix
y_predict = clf.predict(X_test)
cnf_matrix = ConfusionMatrix(y_test, y_predict)
cnf_matrix.plot()
plt.show()
print()

#prediction of new sample
predictions = clf.predict_proba([23,5,10])
print('decision tree prediction: ', predictions)
print()
print()


'''kNN'''
print('KNN')
neigh = KNeighborsClassifier(n_neighbors=3)
neigh = neigh.fit(X_train, y_train)

#cross-validation                                                                       
score = cross_val_score(neigh, X_test, y_test, cv=10)
print('cross-validation score:',score)

#ROC cirve
test_predictions = clf.predict_proba(X_test)
fpr, tpr,thresholds = roc_curve(y_test,test_predictions[:,1:2])
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC curve')
plt.show()
print()

#confusion matrix
y_predict = clf.predict(X_test)
cnf_matrix = ConfusionMatrix(y_test, y_predict)
cnf_matrix.plot()
plt.show()
print()

#prediction of hypothesis
predictions = neigh.predict_proba([23,5,10])
print('kNN prediction: ', predictions)
print()
print()


'''Naive Bayes'''
print('Naive Bayes')
clf = GaussianNB()
clf = clf.fit(X_train, y_train)

#cross-validation                                                                       
score = cross_val_score(clf, X_test, y_test, cv=10)
print('cross-validation score:',score)
print()

#ROC cirve
test_predictions = clf.predict_proba(X_test)
fpr, tpr,thresholds = roc_curve(y_test,test_predictions[:,1:2])
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC curve')
plt.show()
print()

#confusion matrix
y_predict = clf.predict(X_test)
cnf_matrix = ConfusionMatrix(y_test, y_predict)
cnf_matrix.plot()
plt.show()
print()

#prediction of hypothesis
predictions = clf.predict_proba([23,5,10])
print('Naive Bayes prediction: ',predictions)
print()
print()


'''Random Forest'''
print('Random Forest')
clf = RandomForestClassifier(n_estimators=5)
clf = clf.fit(X_train, y_train)

#cross-validation                                                                       
score = cross_val_score(clf, X_test, y_test, cv=10)
print('cross-validation score:',score)
print()

#ROC cirve
test_predictions = clf.predict_proba(X_test)
fpr, tpr,thresholds = roc_curve(y_test,test_predictions[:,1:2])
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC curve')
plt.show()
print()

#confusion matrix
y_predict = clf.predict(X_test)
cnf_matrix = ConfusionMatrix(y_test, y_predict)
cnf_matrix.plot()
plt.show()
print()

#prediction of hypothesis
predictions = clf.predict_proba([23,5,10])
print('Randome Forest prediction: ',predictions)
print()
print()


'''SMV'''
'''
print('SMV')
clf = SVC()
clf = clf.fit(X_train, y_train)
#cross-validation                                                                       
score = cross_val_score(clf, X_test, y_test, cv=10)
print('cross-validation score:',score)
print()

#ROC cirve
test_predictions = clf.predict_proba(X_test)
fpr, tpr,thresholds = roc_curve(y_test,test_predictions[:,1:2])
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC curve')
plt.show()
print()

#confusion matrix
y_predict = clf.predict(X_test)
cnf_matrix = ConfusionMatrix(y_test, y_predict)
cnf_matrix.plot()
plt.show()
print()

#prediction of hypothesis
predictions = clf.predict([23,5,6])
print('SMV prediction: ',predictions)
print()
print()
'''


'''Hypothesis 2'''
print('-------Hypothesis 2 test-------')
t_test = stats.ttest_ind(a= dataChicagoCrime['time_hour'],b= dataMontgomeryCrime['time_hour'],equal_var=False)
print('Hypothesis: the time that crime most likely happens in Chicago is same as Montgomery')
print(t_test)
print()
print()



'''Hypothesis 3'''
print('-------Hypothesis 3 test-------')
# On Tuesday, the probability of a driving under the influnce happens in Silver Spring from 16:00pm to 18:00pm is high.
'''Logistical Regression'''
myDataFrame = pd.concat([dataMontgomeryCrime['day_of_week'], dataMontgomeryCrime['cityNum'],dataMontgomeryCrime['time_section'], dataMontgomeryCrime['narrative']], axis=1)
myDataFrame = myDataFrame.dropna()
# add "affair" column: 1 represents having affairs, 0 represents not
myDataFrame['affair'] = (myDataFrame.narrative == 'DRIVING UNDER THE INFLUENCE').astype(int)

# create dataframes with an intercept column and dummy variables for time_section
y, X = dmatrices('affair ~ day_of_week + cityNum + C(time_section)', myDataFrame, return_type="dataframe")

# flatten y into a 1-D array
y = np.ravel(y)

# instantiate a logistic regression model, and fit with X and y
model = LogisticRegression()
model = model.fit(X, y)

predict_prob = model.predict_proba(np.array([1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 20]))
print('Logistical Regression')
print('On Tuesday, the probability of a driving under the influnce happens in Silver Spring from 16:00pm to 18:00pm is')
print(predict_prob[0][1])
print()
print()



'''Hypothesis 4'''
print('-------Hypothesis 4 test-------')
'''t_test'''
t_test = stats.ttest_ind(a= dataMontgomeryCrime['day_of_week'],b= dataChicagoCrime['weekdayNum'],equal_var=False)
print('Hypothesis 3: the day of week that crime most likely happens in Chicago is same as Montgomery')
print(t_test)
print()