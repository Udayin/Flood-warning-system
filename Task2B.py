# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
from floodsystem.station import *
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key
from floodsystem.flood import stations_level_over_threshold


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations) 
    
    print(stations_level_over_threshold(stations, 0.8))
    


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")

    run()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
#for station in stations:
        #if station.typical_range == None:
            #return None
        #if station.latest_level == None: 
            #return None
        #else:
            #print("Station name and relative water level: {}, {}".format(station.name, station.relative_water_level()))
            #print((station.latest_level - station.typical_range[0]) / (station.typical_range[1] - station.typical_range[0]))
            #print (station.relative_water_level())
    
#latest = self.latest_level
#high = self.typical_range[1]
#low = self.typical_range[0]

# print("Station name and current level: {}, {}".format(station.name,
                                                                #  station.latest_level))

# MY PROBLEM: build_station_list() RETURNS AN EMPTY LIST
# HAVE I DEFINED update_water_levels PROPERLY??


     # function that returns a list of tuples, where each tuple holds 
     # (1) a station at which the latest relative water level is over tol 
     # and (2) the relative water level at the station. 
     # The returned list should be sorted by the relative level in descending order.