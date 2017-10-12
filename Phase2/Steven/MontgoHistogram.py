import numpy as np
import matplotlib.pyplot as plt
import pandas as pd




############################################################################### read crime text file 


#myData=pd.read_json("c:/Users/MC/Google Drive/Another Project/crime.txt")


############################################################################### 
###############################################################################



Cities=['SILVER SPRING','BETHESDA','GAITHERSBURG','SANDY SPRING','CHEVY CHASE',  #the list of the unqiue cities in the data
 'TAKOMA PARK', 'DERWOOD', 'ROCKVILLE', 'GERMANTOWN', 'KISSIMMEE', 'CLARKSBURG',
 'SPENCERVILLE', 'BURTONSVILLE', 'WASHINGTON GROVE', 'LAUREL', 'HYATTSVILLE',
 'MONTGOMERY VILLAGE', 'DAMASCUS', 'KENSINGTON', 'POTOMAC', 'POOLESVILLE',
 'OLNEY', 'BELTSVILLE', 'MOUNT AIRY', 'BROOKEVILLE', 'UNIVERSITY PARK',
 'GLEN ECHO', 'BOYDS', 'WASHINGTON', 'FREDERICK', 'MCG', 'DICKERSON', 'PG',
 'MT AIRY', 'WHEATON', 'CABIN JOHN', 'BRENTWOOD', 'BRINKLOW', 'ASHTON',
 'COLLEGE PARK', 'ADELPHI', 'MONROVIA', 'BARNESVILLE', 'BEALLSVILLE', 'HIGHLAND',
 'WOODBINE', 'TP', 'UPPER MARLBORO']


Frequency=[58687, 11948, 23570, 294, 3664, 5394, 2032, 21970, 15331, 2, 1368,    #the list of the frequency of each city respectively
           93, 2058, 14, 34, 8, 5012, 1332, 2600, 3580, 576, 2500, 2, 43, 589, 
           1, 43, 676, 8, 1, 2, 159, 12, 1, 8, 108, 1, 27, 158, 1, 1, 1, 17, 
           23, 1, 3, 52, 1]



###############################################################################
###############################################################################



#CityList=pd.unique(myData["city"].ravel())                                     #I used this to find the unique cities in the dataset                 
#print(CityList)                                                                #finding the unique number of cities in the column




#FrequencyCity=[]                                                               #I used this to find each frequency of the cities 
#UniqueCity = myData['city']    


#for City in Cities:                                                            #Each city in the list "Cities"
#    Count=0                                                                    #Initial Count is set to 0
#    for i in range(0,len(UniqueCity)):                                         #iterating through the column 
#        if UniqueCity[i] == City:                                              #checking every row is equal to each city in the list 
#            Count += 1                                                         #if that row is the same to the city add one to the count
#    FrequencyCity.append(Count)
#    
#print(FrequencyCity)



###############################################################################
############################################################################### histogram of the first 10 cities

                                                #http://stackoverflow.com/questions/5926061/plot-histogram-in-python

Cities1=Cities[0:10]
Frequency1=Frequency[0:10]                      


pos = np.arange(len(Cities1))    #Traditional dataframe.hist() does not work on our dataset. I looked up online to find ways to create a histogram
width = 1.0                      #This is one of the manual ways to create a histogram using bar graph
plt.figure(figsize=(12,12))      #set figure size big enough to see 
ax = plt.axes()
ax.set_xticks(pos + (width / 2))  #setting xticks 
ax.set_xticklabels(Cities1)       #setting xtick labels 
plt.rc('xtick', labelsize=9)      #xtick font size
plt.bar(pos, Frequency1, width, color='r')   #creating histogram using bar graph 
plt.show()   




############################################################################### 
############################################################################### histogram of the second 10 cities




Cities2=Cities[10:20]                
Frequency2=Frequency[10:20]


pos = np.arange(len(Cities2))
width = 1.0    
plt.figure(figsize=(12,12))
ax = plt.axes()
ax.set_xticks(pos + (width / 2))
ax.set_xticklabels(Cities2)
plt.ylim([0,60000])             #setting yaxis limit consistent to 0,60000 so that it is comparable to each histogram
plt.bar(pos, Frequency2, width, color='r')
plt.show()




############################################################################### 
############################################################################### histogram of the third 10 cities



Cities3=Cities[20:30]                      
Frequency3=Frequency[20:30]


pos = np.arange(len(Cities3))
width = 1.0    
plt.figure(figsize=(12,12))
ax = plt.axes()
ax.set_xticks(pos + (width / 2))
ax.set_xticklabels(Cities3)
plt.ylim([0,60000])
plt.bar(pos, Frequency3, width, color='r')
plt.show()



############################################################################### 
############################################################################### histogram of the fourth 10 cities



Cities4=Cities[30:40]                 
Frequency4=Frequency[30:40]


pos = np.arange(len(Cities4))
width = 1.0    
plt.figure(figsize=(12,12))
ax = plt.axes()
ax.set_xticks(pos + (width / 2))
ax.set_xticklabels(Cities4)
plt.ylim([0,60000])
plt.bar(pos, Frequency4, width, color='r')
plt.show()




############################################################################### 
############################################################################### histogram of the last 8 cities



Cities5=Cities[40:48]
Frequency5=Frequency[40:48]


pos = np.arange(len(Cities5))
width = 1.0    
plt.figure(figsize=(12,12))
ax = plt.axes()
ax.set_xticks(pos + (width / 2))
ax.set_xticklabels(Cities5)
plt.ylim([0,60000])
plt.bar(pos, Frequency5, width, color='r')
plt.show()




###############################################################################
###############################################################################