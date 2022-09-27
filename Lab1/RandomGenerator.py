import math
import random
import numpy as np
import matplotlib.pyplot as plt
import statistics

lambd = 75
number = 1000

def exp_rand(lamb):
    random.seed()
    u = random.random()
    distr = -(1/lambd) * math.log(1-u)
    return distr

def exp_rand_time_span(lamb, time):
    arrival_time_arr = []
    run_sum = 0
    while(len(arrival_time_arr) < 100000 and run_sum < 1000):
        run_sum += exp_rand(lamb)
        arrival_time_arr.append(run_sum)
    return arrival_time_arr

dist = exp_rand_time_span(lambd, number)
mean = statistics.mean(dist)
varianc = statistics.variance(dist)

count, bins, ignored = plt.hist(dist, 14, density=True)
plt.show()
print(mean)
print(varianc)
