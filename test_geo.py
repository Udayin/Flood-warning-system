#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 17:16:43 2017

@author: udayinadukia
"""
from floodsystem.geo import stations_by_distance, stations_within_radius
from floodsystem.stationdata import build_station_list



def test_stations_by_distance():
    
    stations = build_station_list()
    
    listofstations = stations_by_distance(stations,(52.2053, 0.1218))
    
    assert listofstations[:10] == [('Cambridge Jesus Lock', 'Cambridge', 0.8402364350834995), ('Bin Brook', 'Cambridge', 2.502274086951454), ("Cambridge Byron's Pool", 'Grantchester', 4.0720438555077125), ('Cambridge Baits Bite', 'Milton', 5.115589516578674), ('Girton', 'Girton', 5.227070345811418), ('Haslingfield Burnt Mill', 'Haslingfield', 7.044388165868453), ('Oakington', 'Oakington', 7.128249171700346), ('Stapleford', 'Stapleford', 7.265694306995238), ('Comberton', 'Comberton', 7.7350743760373675), ('Dernford', 'Great Shelford', 7.993861351711722)] 
    

def test_stations_within_radius():
    
        stations= build_station_list()
        
        listofstations = stations_within_radius(stations,(52.2053, 0.1218), 10)
        
        assert listofstations == ['Bin Brook', 'Cambridge Baits Bite', "Cambridge Byron's Pool", 'Cambridge Jesus Lock', 'Comberton', 'Dernford', 'Girton', 'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford']