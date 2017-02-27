# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 19:24:44 2017

@author: Louise Aumont
"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood_warning import rate_of_increase
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.flood import stations_highest_rel_level
from floodsystem.flood_warning import prediction
from floodsystem.station import MonitoringStation

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    #build empty lists
    severe_risk = []
    hi_risk = []
    mod_risk = []
    lo_risk = []
    stations_need_further_investigation = []
    
    for station in stations:

        if station.typical_range_consistent():
            if type(station.latest_level) == float and station.latest_level > 0.5:
                dt = 5
        
                dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        
                two_day_predicted_rel_height = prediction(2, dates, levels, 3, station)
                seven_day_predicted_rel_height = prediction(7, dates, levels, 3, station)
        
                if not two_day_predicted_rel_height or not seven_day_predicted_rel_height:
                    pass
        
                elif two_day_predicted_rel_height > 2:
                    severe_risk += [station.name]
                elif seven_day_predicted_rel_height > 2 or two_day_predicted_rel_height > 1:
                    hi_risk += [station.name]
                elif seven_day_predicted_rel_height > 1:
                    mod_risk += [station.name]
                else:
                    lo_risk += [station.name]
            else:
                stations_need_further_investigation += [station.name]
    print("""***Stations with severe risk***""")
    print(severe_risk)
    print('\n')
    print("""***Stations with high risk***""")
    print(hi_risk)
    print('\n')
    print("""***Stations with moderate risk***""")
    print(mod_risk)
    print('\n')
    print("""***Stations with low risk***""")
    print(lo_risk) 
    print('\n')
    print("""***Stations that need further inverstigation***""")
    print(stations_need_further_investigation)




if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")

    run()