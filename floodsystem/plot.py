#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 12:10:57 2017

@author: Terry
"""

import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit
import numpy as np
import datetime
import matplotlib
from floodsystem.station import MonitoringStation

def plot_water_levels(station, dates, levels, typical_low, typical_high):
    '''a function that displays a plot (using Matplotlib) 
    of the water level data against time for a station, and 
    include on the plot lines for the typical low and high levels.
    The axes should be labelled and use the station name as the plot 
    title.'''
    # Plot
    plt.plot(dates,levels)
    plt.axhline(typical_high)
    plt.axhline(typical_low)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Water Levels over the past 10 days:" + station)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    '''a function that plots the water level data and the best-fit 
    polynomial'''
    plt.plot (dates, levels, label = "Actual Water Levels")
    x = matplotlib.dates.date2num(dates)
    x1 = np.linspace(x[0], x[-1], 30)
    poly = polyfit(dates, levels, p)[0]
    plt.plot(x1, poly(x1 - x[0]), label = "Best-fit Polynomial")
    if station.typical_range_consistent():
        plt.plot([dates[0], dates[-1]], [station.typical_range[0], station.typical_range[0]],label = "Typical range - low")
        plt.plot([dates[0], dates[-1]], [station.typical_range[1], station.typical_range[1]],label = "Typical range - high")
    plt.xlabel('time')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Water Levels with Best-fit Polynomial:" + station.name)
    plt.legend(loc='upper left')
    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()