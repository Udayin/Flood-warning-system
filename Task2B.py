# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 18:09:52 2017

@author: Louise Aumont
"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold

def run():

    stations = build_station_list()
    
    update_water_levels(stations)

    x = stations_level_over_threshold(stations, 0.8)

    for i in x:
        station_name, relative_level = i  
        print (station_name, ":", relative_level)


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")

    run()
    


