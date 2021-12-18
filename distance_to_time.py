import math
from decimal import Decimal

def dist_to_time(deliver_a, deliver_b):
    
    if deliver_a.lat == deliver_b.lat and deliver_a.long == deliver_b.long and deliver_a.addr !=  deliver_b.addr:
        return 1

    lat_a = Decimal(deliver_a.lat)
    lat_b = Decimal(deliver_b.lat)
    lon_a = Decimal(deliver_a.long)
    lon_b = Decimal(deliver_b.long)

    phi_1 = math.radians(lat_a)
    phi_2 = math.radians(lat_b)
    delta_phi = math.radians(lat_b - lat_a)
    delta_lambda = math.radians(lon_b - lon_a)

    temp = math.pow(math.sin(delta_phi / 2.0), 2) + math.cos(phi_1) * math.cos(phi_2) * math.pow(math.sin(delta_lambda / 2.0), 2)
    unit = 2 * math.asin(math.sqrt(temp))
    one = 6371000 * unit
    res = round((one/ 1000.0), 3)
    seconds = round((60 * res), 2)

    return seconds