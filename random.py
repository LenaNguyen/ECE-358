import numpy as np
import matplotlib.pyplot as plt
import statistics

lambd = 75
number = 1000

distr = np.random.exponential(1/lambd,number)

mean = statistics.mean(distr)
varianc = statistics.variance(distr)

count, bins, ignored = plt.hist(distr, 14, density = True)
plt.show()