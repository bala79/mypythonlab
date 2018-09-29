from matplotlib import pyplot
import random

x_values = [1,2,3,4,5,6,6,7,8,9]

y_values = [random.randint(0,30) for elt in x_values]

pyplot.plot(x_values,y_values,"o-")

pyplot.xlabel("Value")
pyplot.ylabel("Time")
pyplot.title("My Plot")
pyplot.show()
