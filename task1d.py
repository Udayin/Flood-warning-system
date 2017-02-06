#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 18:32:43 2017

@author: Terry
"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def run():
    
    rivers = rivers_with_station(build_station_list())
    rivers1 = sorted(rivers)
    print (rivers1[:10])
    
    stations = stations_by_river(build_station_list())
    def river(x):
        stations1 = sorted(stations[x])
        return stations1
    print(river('River Aire'), river('River Cam'), river('Thames'))
    
    if __name__ == "__main__":
      print ("*** Task 1D: CUED Part IA Flood Warning System ***")
run()
    
    
    
    
    
    
    
    
    
    