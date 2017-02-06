"""This module contains a collection of functions related to
geographical data."""


from math import radians, cos, sin, asin, sqrt
from .utils import sorted_by_key

AVG_EARTH_RADIUS = 6371  # in km

def haversine(point1, point2, miles=False):
    """ Calculate the great-circle distance between two points on the Earth surface.
    :input: two 2-tuples, containing the latitude and longitude of each point
    in decimal degrees.
    Example: haversine((45.7597, 4.8422), (48.8567, 2.3508))
    :output: Returns the distance bewteen the two points.
    The default unit is kilometers. Miles can be returned
    if the ``miles`` parameter is set to True.
    """
    # unpack latitude/longitude
    lat1, lng1 = point1
    lat2, lng2 = point2

    # convert all latitudes/longitudes from decimal degrees to radians
    lat1, lng1, lat2, lng2 = map(radians, (lat1, lng1, lat2, lng2))

    # calculate haversine
    lat = lat2 - lat1
    lng = lng2 - lng1
    d = sin(lat * 0.5) ** 2 + cos(lat1) * cos(lat2) * sin(lng * 0.5) ** 2
    h = 2 * AVG_EARTH_RADIUS * asin(sqrt(d))
    if miles:
        return h * 0.621371  # in miles
    else:
        return h  # in kilometers

def stations_by_distance(stations, p):
    stations_list = []
    for s in stations:
        stations_list.append((s.name, s.town, haversine((s.coord), (p)))) 

    sorted_stations_list = sorted_by_key(stations_list, 2)
      
    return sorted_stations_list
    
def stations_within_radius(stations, centre, r):
    stations_list= []
    a= stations_by_distance(stations, centre)
    for s in a:
        if s[2]<r:
            stations_list.append(s[0])
    return sorted(stations_list)            #Returns the list sorted

"""task 1d"""
def rivers_with_station(stations):
    results2 = []
    for station in stations:
        river = station.river
        results2.append(river)
    results2 = set(results2)
    return results2
    
def stations_by_river(stations):
    dict = {}
    for s in stations:
        if s.river not in dict:
            dict[s.river]=[s.name]
        elif s.river in dict:
            dict[s.river] += [s.name]
    return dict
    

"""task 1e"""
def rivers_by_station_number(stations, N):
    n = N
    results2=[]
    results3=[]
    results4=[]
    for station in stations:
        river = station.river
        results2.append(river)
    results3 = set(results2)
    for r in results3:
        number = results2.count(r)
        results4.append((number,r))
    ans = sorted(results4, reverse = True)
    
    #print(ans[n-1][0])
    
    while ans[n-1][0] == ans[n][0]:
        n = n+1
    
    
    return ans[:n]
