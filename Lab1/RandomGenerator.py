import math
import random
import numpy as np
import matplotlib.pyplot as plt
import statistics

lambd = 75
number = 1000


def exp_rand(lamb, num):
    ret = []
    for _ in range(0, num):
        random.seed()
        u = random.random()
        distr = -(1/lambd) * math.log(1-u)
        ret.append(distr)
    return ret


dist = exp_rand(lambd, number)
mean = statistics.mean(dist)
varianc = statistics.variance(dist)

count, bins, ignored = plt.hist(dist, 14, density=True)
plt.show()
print(mean)
print(varianc)
