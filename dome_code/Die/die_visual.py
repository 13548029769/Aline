import matplotlib as mlp
mlp.use("TkAgg")
import matplotlib.pyplot as plt
import pygal
from die import Die

die = Die()
die_2 = Die(10)

roll_results = []
[roll_results.append(die.roll() + die_2.roll()) for value in range(500000)]

frequenceies = []
[frequenceies.append(roll_results.count(value)) for value in range(die.num_sides + die_2.num_sides + 1)]
print(frequenceies)

"""draw a sample line chart"""
# plt.plot(frequenceies,linewidth = 3)
# plt.tick_params(axis='both',labelsize=14)

"""draw a simple point chart"""
# plt.scatter([0,1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15,16],frequenceies, s = 5,edgecolors="None",cmap=plt.cm.Reds)

# show chart
# plt.show()

# Visualize the results
hist = pygal.Bar()
hist.title = "Results of rolling 2 D6 1000 times"
hist.x_labels = [1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15,16]
hist._x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add("D6 + D10", frequenceies)
hist.render_to_file("image/die_visual.svg")
