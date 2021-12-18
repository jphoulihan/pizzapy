def fastest_route_by_order_num(routes, size):

    fast_rut = [0]
    fast_rut_obj = []

    for row in range(size):
        for col in range(size):
            if routes[row][col].time_taken != 0 and not fast_rut.__contains__(routes[row][col].col): #ignores first case where origin and dest are same and inserts if col not in fast list
            
                    fast_rut.append(routes[row][col].col)
                    fast_rut_obj.append(routes[row][col])
                    
                    row = routes[row][col].col
                    col = 0 #traverse row again
        
    # fast_rut = fast_rut[:-1]#starting point of delivery not included
    return fast_rut, fast_rut_obj
