# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 18:01:03 2017

@author: Rose Humphry
"""

from floodsystem.utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    ''' a function that returns a list of tuples, 
    where each tuple holds (1) a station at which the latest
    relative water level is over tol and (2) the relative water
    level at the station. The returned list should be sorted 
    by the relative level in descending order.'''
    stations_over_threshold = []
    for station in stations:
        if type(station.relative_water_level()) == float:
            if station.relative_water_level() > tol:
                station_tup = (station.name, station.relative_water_level())
                stations_over_threshold.append(station_tup)
                stations_over_threshold.sort()
    return stations_over_threshold


def stations_highest_rel_level(stations, N):
    '''A function that takes a list of stations and 
    returns a list of the N stations at which the water level, 
    relative to the typical range, is highest. The list should 
    be sorted in descending order by relative level.'''
    most_at_risk_stations = []
    for station in stations:
        if type(station.relative_water_level()) == float:
            x = station.relative_water_level()
            most_at_risk_stations += [(station, float("{0:.6f}".format(x)))]
        else:
            pass

    sorted_most_at_risk_stations = sorted_by_key(most_at_risk_stations, 1, True)
    return sorted_most_at_risk_stations[:N]

