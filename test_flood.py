# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 17:37:13 2017
@author: Louise Aumont
"""

import pytest
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

def test_stations_level_over_threshold():
    "A test that takes a list of test stations, and asserts that\
    if their latest level is over the threshold, the function adds\
    them to the list of stations over the threshold. I have made the\
    typical range of all three station [0,1] to simplify the assertion\
    as their latest levels will also equal their relative levels."
    test_station1 = MonitoringStation("test-s-id-1","test-m-id-1", "station-1", (1,1), [0,1], "river_1", "town_1")
    test_station2 = MonitoringStation("test-s-id-2","test-m-id-2", "station-2", (2,2), [0,1], "river_1", "town_2")
    test_station3 = MonitoringStation("test-s-id-3","test-m-id-3", "station-3", (3,3), [0,1], "river_2", "town_3")
    test_station1.latest_level = 0.77
    test_station2.latest_level = 0.88
    test_station3.latest_level = None
    test = [test_station1, test_station2, test_station3]
    assert stations_level_over_threshold(test, 0.8) == [('station-2', 0.88)]

def test_stations_highest_rel_level():
    '''A test that takes a list of test stations, and asserts that
    when the function stations_highest_rel_level is applied to the list
    of test stations, the function would return a list of station2 
    first (as this has the highest relative level) and then station1. 
    Station 3 will not be in the list as its latest level is equal to
    'None'.'''
    test_station1 = MonitoringStation("test-s-id-1","test-m-id-1", "station-1", (1,1), [2,3], "river_1", "town_1")
    test_station2 = MonitoringStation("test-s-id-2","test-m-id-2", "station-2", (2,2), [4.5,6.8], "river_1", "town_2")
    test_station3 = MonitoringStation("test-s-id-3","test-m-id-3", "station-3", (3,3), [3.1,10.4], "river_2", "town_3")
    test_station1.latest_level = 0.77
    test_station2.latest_level = 7.9
    test_station3.latest_level = None
    test = [test_station1, test_station2, test_station3]
    assert stations_highest_rel_level(test, 3) == [(test_station2, 1.478261), (test_station1, -1.23)]