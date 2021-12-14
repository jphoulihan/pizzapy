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

    print(dist_to_time(deliveries[0], deliveries[0]))
    print(dist_to_time(deliveries[0], deliveries[1]))
    print(dist_to_time(deliveries[0], deliveries[2]))
    print(dist_to_time(deliveries[0], deliveries[3]))
    print(dist_to_time(deliveries[0], deliveries[4]))


if __name__ == '__main__':
    main()

