import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import itertools
from collections import Counter
import operator
'''
dataFile = open('dataChicagoCrime3.csv','r')
dataChicagoCrime = pd.read_csv(dataFile, sep=',', encoding='latin1')
myDataFrame=pd.concat([dataChicagoCrime['community_area'], dataChicagoCrime['time_section'],dataChicagoCrime['date'],dataChicagoCrime['primary_type']], axis=1)
#myDataFrame.to_csv('data_network.csv', index=False)

myDataFrame['date'] = pd.to_datetime(myDataFrame['date'], coerce=True)
myDataFrame['month'] = myDataFrame['date'].dt.month
myDataFrame = myDataFrame.loc[myDataFrame['month'] == 10] 
myDataFrame = myDataFrame.loc[myDataFrame['primary_type'] == 'SEX OFFENSE'] 
myDataFrame.to_csv('data_network.csv', index=False)
'''

dataFile = open('data_network.csv','r')
dataChicagoCrime = pd.read_csv(dataFile, sep=',', encoding='latin1')
dataOfCommunity = dict(dataChicagoCrime['community_area'].value_counts())


links = []
group = {k: g["community_area"].tolist() for k,g in dataChicagoCrime.groupby("time_section")}
for i in group.keys():
    group[i] = list(set(group[i]))
#print(group)


'''density'''
for i in group.keys():    
    links = links + list(itertools.combinations(group[i], 2))
links = list(set(links))
density = len(links) / (len(dataOfCommunity)*(len(dataOfCommunity)-1)/2)
print('density:')
print(density)
print()


'''degree'''
degree = {}
for i in dataOfCommunity.keys():
    degree[i] = 0
    
for i in degree.keys():
    for j in range(0,len(links)):
        if  links[j][0] == i or i == links[j][1]:
            degree[i] = degree[i]+1
sorted_degree = sorted(degree.items(), key=operator.itemgetter(1),reverse=True)
print('Node degree:(node,degree)')
print(sorted_degree)
print()

#c=Counter(links)
'''centrality'''
print('Degree centrality:(node,degree)')
print(sorted_degree[0])
print()


G=nx.Graph()
G.add_nodes_from(dataOfCommunity.keys())
for f,t in links:
    G.add_edge(f, t)


fig = plt.figure(figsize=(10, 10), dpi=150)
graph_pos=nx.spring_layout(G)
nodesize = [100*n for n in dataOfCommunity.values()]
nx.draw_networkx_nodes(G,graph_pos,node_size=nodesize, alpha=0.5, node_color='blue')
nx.draw_networkx_edges(G,graph_pos,width=1, alpha=0.3,edge_color='blue')
nx.draw_networkx_labels(G, graph_pos, labels=None, font_size=10)
plt.axis('off')
plt.title('Network of communities where happened sex offence')
plt.show()
