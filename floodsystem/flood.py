#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 11:40:44 2017

@author: udayinadukia
"""
from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    k= []
    for i in stations:
        if i.relative_water_level() == None:
            pass
        elif i.relative_water_level() > tol:
            k.append((i, i.relative_water_level()))
    x = sorted_by_key(k,1,reverse= True )
    
    return x
    
    
def stations_highest_rel_level(stations, N):
    
    l= []
    b=stations_level_over_threshold(stations, 0.2)
    for i in b:
        l.append(i[0])
    l_cut = l[:N]
    return l_cut