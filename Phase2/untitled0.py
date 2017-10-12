#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 11:47:10 2016

@author: yuanyaozhang
"""

#######################################
# In-class exercise 6
#
# Network analysis
#
# We are using the networkx library
# It is already installed with Anaconda
# Documentation:
# https://networkx.readthedocs.io/en/stable/
#
# Also using community library
# Installation directions:
# https://bitbucket.org/taynaud/python-louvain
#######################################


import networkx as nx
import matplotlib.pyplot as plt
import community

myNetXGraph=nx.karate_club_graph()

# Prints summary information about the graph
print(nx.info(myNetXGraph))

# Print the degree of each node
print("Node Degree")
for v in myNetXGraph:
    print('%s %s' % (v,myNetXGraph.degree(v)))

# Computer and print other stats    
nbr_nodes = nx.number_of_nodes(myNetXGraph)
nbr_edges = nx.number_of_edges(myNetXGraph)
nbr_components = nx.number_connected_components(myNetXGraph)

print("Number of nodes:", nbr_nodes)
print("Number of edges:", nbr_edges)
print("Number of connected components:", nbr_components)


# Draw the network using the default settings
nx.draw(myNetXGraph)
plt.clf()

# Draw, but change the color to to blue
nx.draw(myNetXGraph, node_color='blue')
plt.clf()

# Compute betweeness and then store the value with each node in the networkx graph
betweenList = nx.betweenness_centrality(myNetXGraph)
nx.set_node_attributes(myNetXGraph, 'betweenness', betweenList)
print();
print("Betweeness of each node")
print(betweenList)


#####################
# Clustering
# Code from: http://perso.crans.org/aynaud/communities/#
#####################
# Conduct modularity clustering
partition = community.best_partition(myNetXGraph)

# Print clusters (You will get a list of each node with the cluster you are in)
print();
print("Clusters")
print(partition)

# Setup colors and graph layout. Then print.
size = float(len(set(partition.values())))
pos = nx.spring_layout(myNetXGraph)
count = 0.
for com in set(partition.values()) :
     count += 1.
     list_nodes = [nodes for nodes in partition.keys()
                                 if partition[nodes] == com]
     nx.draw_networkx_nodes(myNetXGraph, pos, list_nodes, node_size = 50,
                                node_color = str(count / size))
nx.draw_networkx_edges(myNetXGraph,pos, alpha=0.5)
plt.show()

