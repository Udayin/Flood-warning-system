#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 17:13:32 2017

@author: Terry
"""

from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list


def run():
    
    d=inconsistent_typical_range_stations(build_station_list())
    d=sorted(d)
    print(d)
    
if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
run()
    