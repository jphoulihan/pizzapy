import csv
from distance_to_time import dist_to_time
from delivery import Delivery
from route import Route

def main():
    
    with open('../../Downloads/4-orders.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')        
        deliveries = [Delivery(order[0], order[1], order[2], order[3], order[4]) for order in read_csv]
        deliveries.insert(0, Delivery(0, "Apache", 0, 53.38133, -6.59299))

        for i in deliveries:
            print(i.__dict__)

        c_1, c_2 = 0, 0
        routes = []
        while(c_1 < len(deliveries)):
            row = []
            while(c_2 < len(deliveries)):
                time_taken = dist_to_time(deliveries[c_1], deliveries[c_2])
                route = Route(c_1, c_2, time_taken)
                row.append(route)
                c_2 += 1
            routes.append(row)
            c_2 = 0
            c_1 += 1
        
        for i in routes:
            for j in i:
                print(j.__dict__)


if __name__ == '__main__':
    main()

