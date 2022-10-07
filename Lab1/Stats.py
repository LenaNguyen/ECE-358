def mean(list):
    return sum(list) / len(list)

def variance(list):
    m = mean(list)
    n = float(0)

    for item in list:
        n += (item - m) ** 2
    
    return float(n / (len(list)-1))


    