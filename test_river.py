#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 17:13:07 2017

@author: Terry
"""

from floodsystem.geo import rivers_with_station
from floodsystem.station import MonitoringStation

def test_rivers():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (52.2053, 0.1218)
    river = "River A"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, None, river, town)
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-3.0, 70)
    trange = (5, 3.4445)
    river = "River B"
    town = "My Town"
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (52.2053, 0.1218)
    trange = (-2.3, 3.4445)
    river = "River C"
    town = "My Town"
    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (52.2053, 0.1218)
    trange = (-2.3, 3.4445)
    river = "River A"
    town = "My Town"
    s4 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (52.2053, 0.1218)
    trange = (8, 3.4445)
    river = "River E"
    town = "My Town"
    s5 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (52.2053, 0.1218)
    trange = (-2.3, 3.4445)
    river = "River B"
    town = "My Town"
    s6 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    r = [s1,s2,s3,s4,s5,s6]
    a = rivers_with_station(r)
    e = sorted(a)
    
    assert e == ["River A", "River B", "River C", "River E"]