import matplotlib.pyplot as plt
from random_walk import Randomwalk

while True:
    rw = Randomwalk(100)
    rw.fill_walk()
    # plt.figure(figsize=(10,10))
    plt.scatter(rw.x_values,rw.y_values, s=15,c=(0.6,0.2,0.3))
    plt.scatter(0,0,c='green',s = 100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='black',s=100)
    # plt.axes().get_xaxis().set_visible(False)
    plt.show()

    keep_running = input('make walk agin? y/n: ')
    if keep_running == 'n' :
        break