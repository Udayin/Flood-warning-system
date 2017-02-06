#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 17:34:57 2017

@author: Terry
"""

from floodsystem.geo import rivers_by_station_number
from floodsystem.station import MonitoringStation

def test_stationsnumber():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station 1"
    coord = (52.2053, 0.1218)
    river = "River A"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, None, river, town)
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station 2"
    coord = (-3.0, 70)
    trange = (5, 3.4445)
    river = "River B"
    town = "My Town"
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station 3"
    coord = (52.2053, 0.1218)
    trange = (-2.3, 3.4445)
    river = "River C"
    town = "My Town"
    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station 4"
    coord = (52.2053, 0.1218)
    trange = (-2.3, 3.4445)
    river = "River A"
    town = "My Town"
    s4 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station 5"
    coord = (52.2053, 0.1218)
    trange = (8, 3.4445)
    river = "River E"
    town = "My Town"
    s5 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station 6"
    coord = (52.2053, 0.1218)
    trange = (-2.3, 3.4445)
    river = "River B"
    town = "My Town"
    s6 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station 7"
    coord = (52.2053, 0.1218)
    trange = (-2.3, 3.4445)
    river = "River B"
    town = "My Town"
    s7 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station 8"
    coord = (52.2053, 0.1218)
    trange = (-2.3, 3.4445)
    river = "River D"
    town = "My Town"
    s8 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station 9"
    coord = (52.2053, 0.1218)
    trange = (-2.3, 3.4445)
    river = "River B"
    town = "My Town"
    s9 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station 10"
    coord = (52.2053, 0.1218)
    trange = (-2.3, 3.4445)
    river = "River E"
    town = "My Town"
    s10 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    
    a = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]
    
    assert rivers_by_station_number(a,1) == [(4, 'River B')]
    assert rivers_by_station_number(a,2) == [(4, 'River B'), (2, 'River E'), (2, 'River A')]
    assert rivers_by_station_number(a,3) == [(4, 'River B'), (2, 'River E'), (2, 'River A')]