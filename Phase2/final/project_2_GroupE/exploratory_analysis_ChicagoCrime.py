# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 16:12:09 2016

@author: hillarysu
"""

import numpy as np
import pandas as pd
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist
from sklearn.cluster import KMeans

dataFile = open('dataChicagoCrime2.csv','r')
dataChicagoCrime = pd.read_csv(dataFile, sep=',', encoding='latin1')



'''Basic Statistical Analysis'''

print(dataChicagoCrime.describe())
print()

print('\n\nStatistic of Primary Type')
primaryType = dataChicagoCrime['primary_type'].value_counts()
print(primaryType)
print()

print('\n\nStatistic of Day of Week')
dayOfWeek = dataChicagoCrime['day-of-week'].value_counts()
print(dayOfWeek)
print()

print('\n\nStatistic of Time Period')
timePeriod = dataChicagoCrime['time_period'].value_counts()
print(timePeriod)
print()



'''Bin the data'''

def hour(x):
    h, m, s = x.split(':')
    t = int(h) + int(m)/60 + int(s)/360
    return t
dataChicagoCrime['time_hour'] = dataChicagoCrime['time'].apply(hour)
minTimeNum = dataChicagoCrime['time_hour'].min()
maxTimeNum = dataChicagoCrime['time_hour'].max()
bins = np.arange(minTimeNum, maxTimeNum+1, 2)
TimeNumBins = pd.cut(dataChicagoCrime['time_hour'], bins, retbins = True)
print('\n\nBinning time:')
print(TimeNumBins)
TimeNum1=np.digitize(dataChicagoCrime['time_hour'],bins)
TimeNumBinsCounts = np.bincount(TimeNum1)
print('\n\nTime Bin count is:',TimeNumBinsCounts)
print()



'''Histograms'''

primaryType = primaryType.to_dict()
X = np.arange(len(primaryType))
plt.bar(X, primaryType.values(), align='center', width=0.5)
plt.xticks(X, primaryType.keys(),rotation=90)
ymax = max(primaryType.values()) + 1
plt.ylim(0, ymax)
plt.show()

dayOfWeek = dayOfWeek.to_dict()
X = np.arange(len(dayOfWeek))
plt.bar(X, dayOfWeek.values(), align='center', width=0.5)
plt.xticks(X, dayOfWeek.keys())
ymax = max(dayOfWeek.values()) + 1
plt.ylim(0, ymax)
plt.show()


timePeriod = timePeriod.to_dict()
X = np.arange(len(timePeriod))
plt.bar(X, timePeriod.values(), align='center', width=0.5)
plt.xticks(X, timePeriod.keys(),rotation=90)
ymax = max(timePeriod.values()) + 1
plt.ylim(0, ymax)
plt.show()
print('\n\n')


'''Scatterplot'''

cols = ['weekdayNum', 'time_hour','community_area']
myData = dataChicagoCrime.reindex(columns = cols)
scatter_matrix(myData,figsize=(10,10))
plt.show()
print('\n\n')




'''k-means'''

X = dataChicagoCrime['latitude']
Y = dataChicagoCrime['longitude']
myDataFrame=pd.concat([X, Y], axis=1)   #putting X and Y together
myDataFrame=myDataFrame.dropna()
myDataFrame = myDataFrame.as_matrix()

k=5     # the number of cluster you want to see

kmeans = KMeans(n_clusters=k)      #initializing kmeans with k clusters
kmeans.fit(myDataFrame)         

labels=kmeans.labels_           
centroids=kmeans.cluster_centers_    #centroids
#print(centroids)

for i in range(k):
    # select only data observations with cluster label == i
    ds = myDataFrame[np.where(labels==i)]
    # plot the data observations
    plt.plot(ds[:,0],ds[:,1],'o')
    # plot the centroids
    lines = plt.plot(centroids[i,0],centroids[i,1],'kx')
    # make the centroid x's bigger
    plt.setp(lines,ms=15.0)
    plt.setp(lines,mew=2.0)
plt.xlabel('latitude'),plt.ylabel('longitude')
plt.title("KMeans")
plt.show()



'''dbscan'''

Z = np.array(myDataFrame)  #storing myDataFrame in numpy array 

Z = Z[0:1000]    

Z = StandardScaler().fit_transform(Z)

db = DBSCAN(eps=0.3, min_samples=10).fit(Z)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

unique_labels = set(labels)

colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = 'k'

    class_member_mask = (labels == k)

    xy = Z[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=14)

    xy = Z[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=6)

plt.title('DBSCAN')
plt.show()



'''Hierarchical'''

A = linkage(Z, 'ward')

c, coph_dists = cophenet(A, pdist(Z))
plt.figure(figsize=(10,10))
plt.title('Hierarchical Clustering Dendrogram (truncated)')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(
    A,
    truncate_mode='lastp',  # show only the last p merged clusters
    p=13,  # show only the last p merged clusters
    show_leaf_counts=False,  # otherwise numbers in brackets are counts
    leaf_rotation=90.,
    leaf_font_size=12.,
    show_contracted=True,  # to get a distribution impression in truncated branches
)
plt.show()


