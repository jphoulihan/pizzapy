import csv
import operator
import datetime
from distance_to_time import dist_to_time
from print_matrix import print_matrix
from nearest_neighbour import fastest_route_by_order_num
from delivery import Delivery
from route import Route

def main():
    
    with open('../../Downloads/6-orders.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')        
        deliveries = [Delivery(order[0], order[1], order[2], order[3], order[4]) for order in read_csv]
        deliveries.insert(0, Delivery(0, "Apache", 0, 53.38133, -6.59299))
        size = len(deliveries)

        routes = []
        for i in range(size):
            row = []
            for j in range(size):
                time_secs = dist_to_time(deliveries[i], deliveries[j])
                route = Route(i, j, time_secs)
                row.append(route)
            routes.append(row)
        
        print('__Unsorted Time Matrix__')
        print_matrix(routes)
        
        for i in range(size):
            routes[i] = sorted(routes[i], key=operator.attrgetter("time_taken"))
        
        print('\n__Sorted Time Matrix__')
        print_matrix(routes)

        fastest_route, fastest_route_obj = fastest_route_by_order_num(routes, size)
        print(len(fastest_route))
        print('\n__Fastest Route By Order Number__')

        for i in range(size):
            print(fastest_route[i], end=',')
        print('\n')

        for i in fastest_route_obj:
            print(f'[{i.row, i.col}]{i.time_taken}', end='\n')#incorrect output should be [5][4] 435.6 instead of [(1, 5)]422.88

        #[(0, 2)]33.6
        #[(2, 1)]115.08
        #[(1, 5)]422.88
        #[5][4]  435.6
        #[4][6]  420.48
        #[6][3]  76.32

        #total time should be 1500.03

        total_secs = sum(x.time_taken for x in fastest_route_obj[1:])
        print('\n\n')
        print(total_secs)
        conversion = datetime.timedelta(seconds=total_secs)
        converted_time = str(conversion)

        print('\n\n__Total Delivery Time__\n', converted_time)

if __name__ == '__main__':
    main()

