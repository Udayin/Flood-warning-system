#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 11:39:37 2017

@author: Terry
"""

import matplotlib.dates
import numpy as np
import datetime


def rate_of_increase(dates, levels, p):

    """" 
    Takes the polyfit programmed in Task2F and differentiates the polynomial.
    Sub in time for today and find the rate of increase at the latest time.

    """

    x = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(x - x[-1], levels, p)
    poly = np.poly1d(p_coeff)
    derivative = np.polyder(poly)

    return derivative(x[0]-x[-1])

def prediction(days, dates, levels, p, station):

    """"If the station has no levels, ignore it,
    Otherwise, use a similar relationship as v=u+at to predict a height for certain number of days
    """

    if not levels:
        return
        
    predicted_height = levels[0] + rate_of_increase(dates, levels, p)*days

    predicted_rel_height = (predicted_height - station.typical_range[0])/(station.typical_range[1] - station.typical_range[0])
    
    return predicted_rel_height

