import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn import decomposition
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage

from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist

########################################################################



dataFile = open('dataMontgomeryCrime.csv','r')
myData = pd.read_csv(dataFile, sep=',', encoding='latin1')


######################################################################### KMEANS Cluster



Y=myData['latitude']   #assigning latitude to X
X=myData['longitude']   #assigning longitude to Y


X=X.dropna()   #dropping nan in X 
Y=Y.dropna()   #dropping nan in Y

myDataFrame=pd.concat([X, Y], axis=1, join='inner')   #putting X and Y together

k=5     # the number of cluster you want to see

kmeans=KMeans(n_clusters=k)      #initializing kmeans with k clusters
kmeans.fit(myDataFrame)         

labels=kmeans.labels_           
centroids=kmeans.cluster_centers_    #centroids

pca2D=decomposition.PCA(2)           #PCA 2 dimension projection

plot_columns=pca2D.fit_transform(myDataFrame)  #plot columns are transfored to fit myDataFrame

plt.scatter(x=plot_columns[:,0], y=plot_columns[:,1], c=labels)  #setting x-axis and y-axis
plt.title("KMeans")
plt.show()



######################################################################## DBSCAN


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


###################################################################### Hierarchical


A = linkage(Z, 'ward')


c, coph_dists = cophenet(A, pdist(Z))
plt.figure(figsize=(6,6))
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
