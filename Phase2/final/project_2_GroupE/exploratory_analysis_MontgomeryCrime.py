import pandas as pd
import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn import decomposition
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage

from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist


dataMontgomeryCrime = open('dataMontgomeryCrime.csv','r')
dataMontgomeryCrime = pd.read_csv(dataMontgomeryCrime, sep=',', encoding='latin1')


'''Basic Statistical Analysis'''

dataMontgomeryCrime2 = dataMontgomeryCrime.drop(['incident_type','zip_code','latitude','longitude','address_number','case_number','pra','start_date','end_date','date'], axis=1)

print(dataMontgomeryCrime.describe())
print()
print(dataMontgomeryCrime2.mode())

print('\n\nStatistic of Narrative')
Narrative = dataMontgomeryCrime['narrative'].value_counts()
print(Narrative)
print()

print('\n\nStatistic of time_section')
time_section = dataMontgomeryCrime['time_section'].value_counts()
print(time_section)
print()

print('\n\nStatistic of day_of_week')
day_of_week = dataMontgomeryCrime['day_of_week'].value_counts()
print(day_of_week)
print()



'''Bin the data 300-400 is Robbery,400-500 is AGG ASSLT, 500-600 is BURG NO FORCE)'''
#####clean the class of string which is meanless when in numeric
dataMontgomeryCrime1 = dataMontgomeryCrime[dataMontgomeryCrime.incident_type != 'D']
dataMontgomeryCrime1 = dataMontgomeryCrime1[dataMontgomeryCrime.incident_type != 'DMV']
dataMontgomeryCrime1 = dataMontgomeryCrime1[dataMontgomeryCrime.incident_type != 'N']
dataMontgomeryCrime1 = dataMontgomeryCrime1[dataMontgomeryCrime.incident_type != 'M']
dataMontgomeryCrime1 = dataMontgomeryCrime1[dataMontgomeryCrime.incident_type != 'OTH']
dataMontgomeryCrime1 = dataMontgomeryCrime1[dataMontgomeryCrime.incident_type != 'SWR']

dataMontgomeryCrime1['incident_type'] = dataMontgomeryCrime1['incident_type'].astype(int)

minnum = dataMontgomeryCrime1['incident_type'].min()
maxNum = dataMontgomeryCrime1['incident_type'].max()

#after deleting the reluctant data the data start with 11
minNum= minnum - 11

bins = np.arange(minNum, maxNum, 100)
NumBins = pd.cut(dataMontgomeryCrime1['incident_type'], bins, retbins = True)

print('\n\nClass Num:')
pprint(NumBins)
print()
Num1=np.digitize(dataMontgomeryCrime1['incident_type'],bins)
NumBinsCounts = np.bincount(Num1)
print('\n\nClass Num Bin count is:')
pprint(NumBinsCounts)
print()



'''k-means'''

X = dataMontgomeryCrime['latitude']
Y = dataMontgomeryCrime['longitude']
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
print()


'''dbscan'''

Z = np.array(myDataFrame)  #storing myDataFrame in numpy array 

Z = Z[0:5000]    

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
print()


'''Hierarchical'''

A = linkage(Z, 'ward')

c, coph_dists = cophenet(A, pdist(Z))
plt.figure(figsize=(6,6))
plt.title('Hierarchical Clustering Dendrogram (truncated)')
plt.xlabel('sample cluster')
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
