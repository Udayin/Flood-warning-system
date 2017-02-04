#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 11:30:59 2017

@author: udayinadukia
"""
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


stations = build_station_list()

def distance():             #Defining Function
    
    stations = build_station_list()

    listofstations = stations_by_distance(stations,(52.2053, 0.1218)) #Specify coordinates
    
    
    
    return listofstations

print("Closest 10" ,distance()[:10])
print('\n')  #Adding a space
print("Furthest 10" ,distance()[-10:]) 

    
