import pandas

import matplotlib.pyplot as pyplot


dataset = pandas.read_csv("dataset.csv")

print(dataset)

dataset = dataset.values


pyplot.scatter(dataset[:,0],dataset[:,1])
pyplot.savefig("scatterplot.png")
pyplot.close()



