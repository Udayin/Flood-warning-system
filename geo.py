"""This module contains a collection of functions related to
geographical data."""



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