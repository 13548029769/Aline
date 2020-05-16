import matplotlib as mpl
mpl.use("TkAgg")
import matplotlib.pyplot as plt

"""draw a sample line chart"""
# input_value = [1,2,3,4,5]
# squares = [1,4,9,16,25]
# plt.plot(input_value,squares,linewidth = 3)
# # set line chart's tilt, add label to x/y coordinate system
# plt.title("Squares Number", fontsize=24)
# plt.xlabel("Value",fontsize=14)
# plt.ylabel("Square of Value",fontsize=14)
# # set size of tick mark
# plt.tick_params(axis='both',labelsize=14)


"""draw a simple point chart"""
x_values = list(range(1,5000))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, s = 5,edgecolors="None",c=y_values,cmap=plt.cm.Reds)
plt.title("Point Chart",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Squares Value",fontsize = 14)
# set size of tick mark
plt.tick_params(axis='both',which = 'major',labelsize = 0.5)
plt.axis([0,5001,0,125000000000])
# sava chart as image
# plt.savefig("Square plot.png",bbox_inche='tight')



# show chart
plt.show()
