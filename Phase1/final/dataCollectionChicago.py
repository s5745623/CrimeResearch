# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 23:25:04 2016

@author: hillarysu
"""
import pandas as pd
from pprint import pprint

'''collectiong new data'''
url = ("https://data.cityofchicago.org/resource/6zsd-86xi.json?$limit=150000")
dataChicagoCrime = pd.read_json(url)

# remove unnecessary column
dataChicagoCrime = dataChicagoCrime.drop(['fbi_code','id','case_number','updated_on','location'],1)

'''data cleaning'''
missingValues = dataChicagoCrime.isnull().sum()
fraction_MissingValues = missingValues.divide(150000)

'''Feature Generation'''
# crime type and location
dataChicagoCrime['crime_type, location'] = dataChicagoCrime[['primary_type', 'location_description']].apply(tuple, axis=1)

# day of week
dataChicagoCrime['day-of-week'] = dataChicagoCrime['date'].dt.dayofweek
days = {0:'Mon',1:'Tues',2:'Weds',3:'Thurs',4:'Fri',5:'Sat',6:'Sun'}
dataChicagoCrime['day-of-week'] = dataChicagoCrime['day-of-week'].apply(lambda x: days[x])

# location
dataChicagoCrime['location_cooedinate'] = dataChicagoCrime[['latitude', 'longitude']].apply(tuple, axis=1)

# change column order
cols = ['year', 'date', 'day-of-week', 'iucr', 'primary_type', 'description', 'domestic', 'location_description', 'block', 'ward', 'community_area', 'x_coordinate', 'y_coordinate', 'latitude', 'longitude', 'location_cooedinate', 'beat', 'district', 'crime_type, location','arrest']
dataChicagoCrime = dataChicagoCrime.reindex(columns = cols)
# sort by date
dataChicagoCrime = dataChicagoCrime.sort_values('date')

pprint(dataChicagoCrime)


