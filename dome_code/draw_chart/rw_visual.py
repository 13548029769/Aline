import matplotlib as mpl

mpl.use("TkAgg")
import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    plt.figure(dpi=128, figsize=(10, 6))
    point_nums = list(range(rw.num_points))
    # plt.scatter(rw.x_value, rw.y_value, s=0.1, c=point_nums, cmap=plt.cm.Reds, edgecolors='None')
    # plt.scatter([0],[0], s=5, c="green",edgecolors='None')
    # plt.scatter(rw.x_value[-1], rw.y_value[-1], s=5, c='blue', edgecolors='None')

    plt.plot(rw.x_value, rw.y_value, linewidth=1, color="gold")
    plt.plot([0], [0], linewidth=10, color="red")
    plt.plot(rw.x_value[-1], rw.y_value[-1], linewidth=10, color="red")

    # hide coordinate axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n):\n")
    if keep_running != 'y':
        break
