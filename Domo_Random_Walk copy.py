from random import seed
from random import random
from matplotlib import pyplot
from pandas.plotting import autocorrelation_plot

# Domo Closing Price Data
domo = [15.78, 17.030001, 16.700001, 17.1, 17.959999, 17.389999, 19.16, 18.299999, 18.469999, 18.200001, 17.67, 17.309999, 16.309999, 16.290001, 15.18, 14.41, 13.83, 13.15, 14.6, 16.18, 15.1, 15.56, 14.06, 13.65, 13.59, 13.34, 13.06, 13.97,
        13.28, 13.29, 13.41, 14.3, 14.84, 15.22, 14.62, 14.9, 14.53, 14.89, 17.559999, 15.26, 15.94, 16.610001, 16.01, 16.549999, 14.44, 14.55, 14.61, 14.09, 13.23, 12.25, 12.75, 14.35, 14.24, 14, 14.2, 12.79, 12.46, 12.78, 12.73, 12.82, 14.05, 14.21]

initial_point = domo[45]
print(initial_point)
# create random walk
seed(1)

# creates empty list names random walk
random_walk = list()

# adds -1 to random_walk list if random number was below .5 else add 1 to list
# random_walk.append(-1 if random() < 0.5 else 1)
random_walk.append(initial_point)
# 100 iterations
for i in range(1, 1000):

    # calculates + or - 1
    movement = -1 if random() < 0.5 else 1

    # Adds to next value in the list
    value = random_walk[i-1] + movement

    # adds value to list
    random_walk.append(value)

# take difference
# creates empty list names diff
diff = list()

# sorts from 0 to length of list random_walk
for i in range(1, len(random_walk)):
    # finds difference between start and next
    value = random_walk[i] - random_walk[i - 1]
    # appends difference to diff list
    diff.append(value)

# line plot
# plot difference
# pyplot.plot(diff)
pyplot.plot(random_walk)
pyplot.title("Domo Stock")
pyplot.xlabel("Days")
pyplot.ylabel("Price")
pyplot.show()
