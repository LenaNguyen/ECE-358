import math
import numpy as np


def gen_exponential_val(_lambda):
    u = np.random.uniform(0, 1)
    return -(1/_lambda) * math.log(1-u)
