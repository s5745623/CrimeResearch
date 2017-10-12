import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

############################################################################### Loading csv files



dataFile = open('dataChicagoCrime2.csv','r')
dataChicagoCrime = pd.read_csv(dataFile, sep=',', encoding='latin1')

dataFile = open('dataMontgomeryCrime.csv','r')                                
dataMontgomeryCrime1 = pd.read_csv(dataFile, sep=',', encoding='latin1')       



############################################################################### Defining hour function to use 'time' attribute to convert into hour
                                                                              


def Hour(x):                                                 
    h, m, s = x.split(':')                                                    # split hour minute second
    t = int(h) + int(m)/60 + int(s)/360                                       # dividing minute by 60 and second by 360
    return t

dataChicagoCrime['time_hour'] = dataChicagoCrime['time'].apply(Hour)        # apply hour function to the data


#dataMontgomeryCrime1['time_second'] = dataMontgomeryCrime1['time'].apply(Hour)



###############################################################################


X=dataChicagoCrime['time_hour']                                             # assigning time second to x

Y=dataChicagoCrime['community_area']                                                # assigning district to y

Z=pd.concat([X,Y],axis=1)                                                     # adding X and Y and combine them into Z
Z=Z.values                                                                    # turning panda dataframe to numpy array


A=dataChicagoCrime['weekdayNum']                                              # assigning weekdayNum to A
A=A.values


gnb = DecisionTreeClassifier()      
#models.append(('KNN', KNeighborsClassifier()))                                                      # Naive Bayes model

y_pred = gnb.fit(Z,A).predict(Z)                                              # Predict weekday based on Z


###############################################################################


Z=pd.concat([X,Y],axis=1)                                                     # bringing Z as pandas dataframe again

A=dataChicagoCrime['weekdayNum']                                              # assigning weekdayNum to A


Prediction=pd.DataFrame(y_pred)                                               # making y_pred to a pandas dataframe
Prediction.columns=['prediction']                                             # adding column


Z=pd.concat([Z,A,Prediction],axis=1)                                          # adding time hour, district, weekdayNum, prediction together 
count.plot()
count=Z['prediction'].value_counts()                                          # counting different values of prediction 

print(count)

print("based on time_hour and district, the most of crimes will occur on Fridays by Naive Bayes")

