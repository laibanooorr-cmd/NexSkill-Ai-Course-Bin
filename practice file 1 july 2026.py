import numpy as np

ids, price, long, lat = np.genfromtxt('practice file 1 july 2026.txt', delimiter=';', usecols=(0, 1, 2, 3), unpack=True, dtype=None, skip_header=1)

print("price:")
