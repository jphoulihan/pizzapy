import csv
import operator
from distance_to_time import dist_to_time
from delivery import Delivery
from route import Route

def main():
    
    with open('../../Downloads/4-orders.csv') as csvfile:
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
        
    
        for i in routes:  # outer loop  
            for j in i:  # inner loop               
                print(f'[{j.row}][{j.col}] {j.time_taken}', end = " ") # print the elements  
            print()
        
        for i in range(size):
            print(routes[0][i].time_taken)
        
        print(routes[0][0].time_taken)
        print(routes[0][0])
        
        new_l = sorted(routes[0], key=operator.attrgetter("time_taken"))

        print(new_l[0].time_taken)





if __name__ == '__main__':
    main()

