import numpy as np


def m_m_1_queue():
    _lamdba = 75
    arrival_times = np.random.exponential(1/_lamdba, 1000)
