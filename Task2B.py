#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 11:25:49 2017

@author: udayinadukia
"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold


def run():
    
    stations = build_station_list()
    update_water_levels(stations)
    tuplist = stations_level_over_threshold(stations,0.8)
    
    for i in tuplist:
        print(i[0].name, ":", i[1])
    #print(stations_level_over_threshold(stations, 0.8))
   # for i in tuplist:
     
        

if __name__ == "__main__":
    print("***Task 2B***")        
run()
