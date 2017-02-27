# -*- coding: utf-8 -*-

from floodsystem.station import *
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)
    
    print (stations_highest_rel_level(stations, 10))
    
    

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")

    run()
    
