# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 08:06:02 2016

@author: hillarysu
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-deep')

'''day-of-week'''
dayOfWeek = {1: 31331, 2: 30864, 3: 30447, 4: 31271, 5: 33585, 6: 31837, 7: 31023}
X = np.arange(len(dayOfWeek))

day_of_week = {1: 24442, 2: 26062, 3: 25729, 4: 24516, 5: 25361, 6: 20527, 7: 18883} 
    
p1 = plt.bar(X-0.5, dayOfWeek.values(),  width=0.5, color='y' )
p2 = plt.bar(X, day_of_week.values(), align='center', width=0.5, color='m')
plt.legend((p1[0], p2[0]), ( 'Chicago', 'Montgomery' ),prop={'size':8})
plt.ylabel( 'Crime Count' )
plt.xticks(X, ['Mon', 'Tues', 'Weds', 'Thurs', 'Fri', 'Sat', 'Sun'])
ymax = 40000
plt.ylim(0, ymax)
plt.show()


'''time section'''
timePeriod = {1: 17176,2: 10156,3: 7385,4: 11202, 5: 18100,6: 21200, 7: 21463,8: 22945,9: 23917, 10: 24630, 11: 23444, 12: 18740}
X = np.arange(len(timePeriod))
print(timePeriod.values())

time_section = {1.0: 11199, 2.0: 7505, 3.0: 3258, 4.0: 10330, 5.0: 15893, 6.0: 17328, 7.0: 17385, 8.0: 18111, 9.0: 18167, 10.0: 16507, 11.0: 15274, 12.0: 14454}
print(time_section.values())
p1 = plt.bar(X-0.5, timePeriod.values(),  width=0.5, color='y' )
p2 = plt.bar(X, time_section.values(), align='center', width=0.5, color='m')
plt.legend((p1[0], p2[0]), ( 'Chicago', 'Montgomery' ),prop={'size':8})
plt.ylabel( 'Crime Count' )
plt.xticks(X, ['0:00-2:00', '2:00-4:00', '4:00-6:00', '6:00-8:00', '8:00-10:00', '10:00-12:00', '12:00-14:00', '14:00-16:00', '16:00-18:00', '18:00-20:00', '20:00-22:00','22:00-24:00'],rotation=90)
ymax = 30000
plt.ylim(0, ymax)
plt.show()
