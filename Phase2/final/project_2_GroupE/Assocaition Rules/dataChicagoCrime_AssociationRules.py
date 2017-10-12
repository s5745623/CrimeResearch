#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 15:29:37 2016

@author: yuanyaozhang
"""

import Orange
from orangecontrib.associate.fpgrowth import *  

table = []
with open("dataChicagoCrime_AssociationRules.csv", "r") as f:
	for line in f.readlines():
		table.append( line.replace("\n","").split(",") )

titles = table[0]
data = table[1:]

dic = set();

for t in ["primary_type","day-of-week","community_area"]:
	ind = titles.index( t )
	for i in range( len(data) ):
		dic.add( data[i][ind] )

dicl = list( dic )

for t in ["primary_type","day-of-week","community_area"]:
	ind = titles.index( t )
	for i in range( len(data) ):
		if data[i][ind] == '':
			data[i][ind] = -1
		else: 
			data[i][ind] = dicl.index( data[i][ind] )


itemsets = frequent_itemsets(data, 660)


result = list(itemsets)

result = sorted( result, key= lambda record: -record[1] ) 

print( "-----------------------total rules num: " + str( len(result) ) + "--------------------------\n" )

for i in range( len(result) ):
	if len(result[i][0]) > 2:
		it = list(result[i][0])
		for j in range( len(it) ):
			it[ j ]= dicl[ it[j] ]
		print( str(it) + ":" + str( result[i][1] ) )


