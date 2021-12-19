import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText

def plot_coords(fast_rut_obj, fastest_rut, deliveries, size):

    x = [x.row for x in fast_rut_obj]
    y = [y.col for y in fast_rut_obj]
    addr_list = [deliveries[i].addr for i in fastest_rut]#use route index to get delivery object address
        
    font = {'family': 'sans-serif',
        'color':  'mediumseagreen',
        'weight': 'heavy',
        'size': 30,
        }

    plt.figure(figsize=(size, size), facecolor='lightcyan')
    plt.title("Delivery Route", fontdict=font)
    plt.plot(x, y, 'o-', color='lightgreen', alpha=0.75)

    c = 0
    for i,j in zip(x,y):

        c+=1
        label = f'({c}) {addr_list[j]}'
        plt.annotate(label, # this is the text
                     (i,j), # these are the coordinates to position the label
                     textcoords="offset points", # how to position the text
                     xytext=(0,10), # distance from text to points (x,y)
                     ha='center', # horizontal alignment can be left, right or center
                     weight='heavy'
                    )

    plt.show()

