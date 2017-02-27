# -*- coding: utf-8 -*-

from floodsystem.station import *
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key

def stations_level_over_threshold(stations, tol=0):
    """ Function that takes a list of stations and a tolerance 
    and returns the list of tuples (name of station with relative water level over tolerance, relative water level)"""
    S = []
    update_water_levels(stations)
    for station in stations:
        if station.relative_water_level() == None:
            pass
        if type(station.relative_water_level()) == float:
            if station.relative_water_level() > tol:
                S += [(station.name, station.relative_water_level())]
    return sorted_by_key (S, 1, reverse = True)

    
    
    
    
def stations_highest_rel_level(stations, N):
    S = stations_level_over_threshold(stations, tol=0)
    return S[:N-1]