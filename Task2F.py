# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 13:11:25 2017

@author: Louise Aumont
"""
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib
import datetime
import matplotlib.pyplot as plt
from floodsystem.station import MonitoringStation
import numpy as np

def run():

    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    five_stations_with_highest_current_levels = stations_highest_rel_level(stations, 5)

    for i in five_stations_with_highest_current_levels:
        dt=3
        station, relative_level = i
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_level_with_fit(station, dates, levels, 4)
        
        
        
if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")

    run()
