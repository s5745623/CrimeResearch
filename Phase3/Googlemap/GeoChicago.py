#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 12:26:05 2016

@author: yuanyaozhang
"""

import pandas as pd
import numpy as np
from pprint import pprint
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, PanTool, WheelZoomTool, BoxSelectTool, HoverTool
)

API_KEY="AIzaSyBZha7DKqyZDkEBIdsMh1ESZzxXnkZLcYw"

dataChicagoCrime = open('dataChicagoCrimeGeo1.csv','r')
dataChicagoCrime = pd.read_csv(dataChicagoCrime, sep=',', encoding='latin1')



map_options = GMapOptions(lat=41.87, lng=-87.62, map_type="roadmap", zoom=11)

plot = GMapPlot(
    x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options, api_key=API_KEY,
)
plot.title.text = "ChicagoCrimeGeo"

source = ColumnDataSource(
    data=dataChicagoCrime
)


circle = Circle(y="latitude", x="longitude", size=1, fill_color="red", fill_alpha=0.8, line_color=None)
plot.add_glyph(source, circle)

plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool(), HoverTool(tooltips=[("incident number: ", "$index"), ("latitude,longitude", "(@latitude, @longitude)"),
                       ("Date","@date"),("Crime Type", "@primary_type"),("Day of week","@day_of_week")]))
output_file("gmap_chicago.html")
show(plot)