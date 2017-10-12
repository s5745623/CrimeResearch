# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 10:13:48 2016

@author: hillarysu
"""

from bokeh.io import show, output_file
from bokeh.models import (
    GeoJSONDataSource,
    HoverTool,
    LogColorMapper
)
from bokeh.palettes import Viridis6 as palette
from bokeh.plotting import figure

dataFile = open('CommunityAreasNew.geojson','r')
geojson = dataFile.read()
geo_source = GeoJSONDataSource(geojson=geojson)

palette.reverse()
color_mapper = LogColorMapper(palette=palette)

mp = figure(height=600, width=600,tools="tap", title="Crime Data of Chicago,2016")
mp.patches(xs='xs' , ys='ys',fill_color={'field': 'crime_numbe', 'transform': color_mapper},fill_alpha=0.7, source=geo_source)
mp.multi_line(xs='xs', ys='ys', line_color='white', line_width=0.1, source=geo_source )
mp.add_tools(HoverTool(tooltips=[("Community Name", "@community"),("Community Number", "(@area_numbe)"),("Crime Count", "(@crime_numbe)")]))

output_file("geojson.html")
show(mp)