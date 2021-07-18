from math import radians, cos, sin, asin, sqrt


def haversine(coordinate_first, coordinate_second):

    coordinate_longitude_first = coordinate_first[0]
    coordinate_latitude_first = coordinate_first[1]

    coordinate_longitude_second = coordinate_second[0]
    coordinate_latitude_second = coordinate_second[1]

    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians,
                                 [coordinate_longitude_first, coordinate_latitude_first, coordinate_longitude_second,
                                  coordinate_latitude_second])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r
