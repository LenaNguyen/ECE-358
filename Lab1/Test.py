import math
import random
import numpy as np
import matplotlib.pyplot as plt
import statistics

lambd = 75
number = 1000


def gen_exponential_val(_lambda):
    u = np.random.uniform(0, 1)
    return -(1/_lambda) * math.log(1-u)


def exp_rand(lamb, num):
    ret = []
    for _ in range(0, num):
        random.seed()
        u = np.random.uniform(0, 1)
        distr = gen_exponential_val(lambd)
        ret.append(distr)
    return ret


dist = exp_rand(lambd, number)
mean = statistics.mean(dist)
varianc = statistics.variance(dist)

count, bins, ignored = plt.hist(dist, 14, density=True)
plt.show()
print(mean)
print(varianc)
