#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 17:29:52 2017

@author: Terry
"""

from floodsystem.geo import stations_by_river
from floodsystem.station import MonitoringStation

def test_stationsbyriver():
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
    
    r = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]
    a = stations_by_river(r)
    def riv(x):
        c = sorted(a[x])
        return c
        
    assert riv("River A") == ['some station 1', 'some station 4']
    assert riv("River B") == ['some station 2', 'some station 6', 'some station 7','some station 9']
    assert riv("River C") == ['some station 3']
    assert riv("River D") == ['some station 8']
    assert riv("River E") == ['some station 10', 'some station 5']