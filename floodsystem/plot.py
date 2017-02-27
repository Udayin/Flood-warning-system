#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 12:10:57 2017

@author: Terry
"""

import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit
import numpy as np
import matplotlib
from floodsystem.utils import sorted_by_key
import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit
from datetime import datetime, timedelta


def plot_water_levels(station, dates, levels):
    '''a function that displays a plot (using Matplotlib) 
    of the water level data against time for a station, and 
    include on the plot lines for the typical low and high levels.
    The axes should be labelled and use the station name as the plot 
    title.'''
    t = dates
    level = levels
    
    #Plot
    plt.plot(t, level)
    

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    Lower, Upper = station.typical_range
    plt.plot(dates, np.full(len(dates), Lower))
    plt.plot(dates, np.full(len(dates), Upper))
    
    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    '''a function that plots the water level data and the best-fit 
    polynomial'''
    x = matplotlib.dates.date2num(dates)
    
    a,b = polyfit(dates, levels, p)
    
    #plot orginal data points
    plt.plot(x, levels, '.')
    
    #plot polynomial fit
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, a(x1-b))
    
    
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.title(station.name)
   
    Lower, Upper = station.typical_range
    plt.plot(Lower, levels)
    plt.plot(Upper, levels)
   
    plt.show()
     
     
     
     
   
    
    
    
    