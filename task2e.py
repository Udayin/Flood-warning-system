#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 00:22:06 2017

@author: Terry
"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def run():

    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    five_stations_with_highest_current_levels = stations_highest_rel_level(stations, 5)

    for i in five_stations_with_highest_current_levels:
        dt=10
        station, relative_level = i
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(station.name, dates, levels, station.typical_range[0], station.typical_range[1])
        print(dates[0])
        print(levels[0])

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")

    run()