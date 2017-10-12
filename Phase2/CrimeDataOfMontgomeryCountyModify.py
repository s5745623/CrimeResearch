#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 22:43:25 2016

@author: yuanyaozhang
"""

import pandas as pd
from pprint import pprint
import datetime

#########collectiong new data##########
#url = ("https://data.montgomerycountymd.gov/resource/yc8a-5df8.json?$$app_token=tX2XTxtf7mZd8F5eQ7enqtsPO")
#dataMontgomeryCrime1 = pd.read_json(url)
#dataMontgomeryCrime1.to_csv('dataMontgomeryCrime.csv')
dataFile = open('dataMontgomeryCrime.csv','r')
dataMontgomeryCrime = pd.read_csv(dataFile, sep=',', encoding='latin1')


#######data cleaning##########
# remove unnecessary column
dataMontgomeryCrime = dataMontgomeryCrime.drop(['incident_id','incident_type','sector','police_district_number'], axis=1)


# fraction of noise values
print('The fraction of noise values:')

District = dataMontgomeryCrime['district'].value_counts()
print(District)
print()
type = dict.fromkeys(dataMontgomeryCrime['district']).keys()
DistrictFrame = dataMontgomeryCrime['district'].isin(type)
noiseValue = len(dataMontgomeryCrime.index) - len(DistrictFrame.index)
fraction_noiseValues = noiseValue / len(dataMontgomeryCrime.index)
print('district noise fraction','\t',fraction_noiseValues)
print()

Narrative = dataMontgomeryCrime['narrative'].value_counts()
print(Narrative)
print()
type = dict.fromkeys(dataMontgomeryCrime['narrative']).keys()
NarrativeFrame = dataMontgomeryCrime['narrative'].isin(type)
noiseValue = len(dataMontgomeryCrime.index) - len(NarrativeFrame.index)
fraction_noiseValues = noiseValue / len(dataMontgomeryCrime.index)
print('narrative noise fraction','\t',fraction_noiseValues)
print()


#numeric
features = ['zip_code','latitude','longitude','address_number','case_number']
for i in features:
    numericValue = pd.to_numeric(dataMontgomeryCrime[i], errors='coerce')
    numericValue = numericValue.dropna()
    noiseValue = len(dataMontgomeryCrime.index) - len(numericValue.index)
    fraction_noiseValues = (noiseValue / len(dataMontgomeryCrime.index))*100
    print(i,'\t',fraction_noiseValues,"%")

#numeric&string
features = ['end_date','start_date','agency','state','location','date','geolocation']
for i in features:
    numericValue = pd.to_numeric(dataMontgomeryCrime[i], errors='coerce')
    numericValue = numericValue.dropna()
    noiseValue = len(numericValue.index)
    fraction_noiseValues = (noiseValue / len(dataMontgomeryCrime.index))*100
    print(i,'\t',fraction_noiseValues,"%")


# narrative, place, address
dataMontgomeryCrime['narrativeCrime, place, address'] = dataMontgomeryCrime[['narrative', 'place','location']].apply(tuple, axis=1)


