#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 13:53:42 2017

@author: Terry
"""

import matplotlib
import numpy as np
import datetime

def polyfit(dates, levels, p):
    " a function that given the water level time history (dates, levels)\
    for a station computes a least-squares fit of polynomial of degree p\
    to water level data. The function should return a tuple of (1) the \
    polynomial object and (2) any shift of the time (date) axis"
    x = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(x - x[0], levels, p)
    poly = np.poly1d(p_coeff)
    return (poly, -x[0])
    