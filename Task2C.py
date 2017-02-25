#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 15:04:37 2017

@author: udayinadukia
"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    
    stations= build_station_list()
    update_water_levels(stations)
    dangerous_stations=stations_highest_rel_level(stations, 10)
    
    for i in dangerous_stations:
        print(i.name, ":", i.relative_water_level())

if __name__ == "_main":
    
    run()