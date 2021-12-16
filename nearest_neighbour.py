import operator

def fastest_route_by_order_num(routes, size):

    short_time = [min(routes[0][1:], key=operator.attrgetter("time_taken"))]
    fastest_route = [short_time[0].col]

    for i in range(size):
        for j in range(size):
            if routes[i][j].time_taken != 0.0 and routes[i][j].col not in fastest_route: #ignores first case where origin and dest are same and inserts if col not in fast list
                fastest_route.append(routes[i][j].col)
                i = routes[i][j].col #jumps to next row where row num == col num
                j = 0 #traverse row again
        
    fastest_route = fastest_route[:-1]
    return fastest_route