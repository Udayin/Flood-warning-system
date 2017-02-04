#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 15:48:57 2017

@author: udayinadukia
"""

from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def radius():
    stations= build_station_list()
    listofstations = stations_within_radius(stations,(52.2053, 0.1218), 10)
    print(listofstations)

radius()