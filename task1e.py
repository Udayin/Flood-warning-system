#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 14:34:48 2017

@author: Terry
"""

from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    a = rivers_by_station_number(build_station_list(), 9)
    print(a)
    
if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
run()

    