"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += " measure id: {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
        
    def typical_range_consistent(self):
        "A function which takes the typical_range of a station and returns\
        true or false depending on whether the data given is consistent\
        or inconsistent"
        if self.typical_range == None:
            return False
        elif self.typical_range[0] > self.typical_range[1]:
            return False
        else:
            return True
        
    def relative_water_level(self):
        "A method that the returns the latest water level as a fraction\
        of the typical range, i.e. a ratio of 1.0 corresponds to a level\
        at the typical high and a ratio of 0.0 corresponds to a level at\
        the typical low"
        if self.typical_range_consistent() and type(self.latest_level) == float :
            return (self.latest_level - self.typical_range[0])/(self.typical_range[1] - self.typical_range[0])
        else:
            return None
            
    def inconsistent_typical_range_stations(stations):
        "A function which takes the stations list and returns a list of stations that have inconsistent data"
        inconsistent_data_list = []
        for station in stations:
            if station.typical_range_consistent():
                pass
        else:
            inconsistent_data_list.append(station.name)
        return inconsistent_data_list
    
 