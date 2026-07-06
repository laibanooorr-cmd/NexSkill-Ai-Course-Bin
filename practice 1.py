import numpy as np

price, bed, bath, acre = np.genfromtxt('RealEstate-USA.csv', delimiter=',', skip_header=1, usecols=(2, 3, 4, 5), dtype=int, encoding=None, unpack=True)

print("price:", price)
print("bed:", bed)
print("bath:", bath)
print("acre:", acre)


print(np.min(price))


print("Real Estate.com price average:", np.average(price))
print("Real Estate.com price mean:", np.mean(price))
print("Real Estate.com price standard deviation:", np.std(price))
print("Real Estate.com price median:", np.median(price))
print("Real Estate.com price percentile - 45:", np.percentile(price,45))
print("Real Estate.com price percentile - 20:", np.percentile(price, 20))

print("Real Estate.com price max:", np.max(price))
print("Real Estate.com price min:", np.min(price))

print("Real Estate.com price square:", np.square(price))
print("Real EState.com price sqrt:", np.sqrt(price))
print("Real Estate.com price pow:", np.pow(price, price))
print("Real Estate.com price abs:", np.abs(price))

pricepi = (price / np.pi) + 1
sin_value = np.sin(pricepi)
print("sin_value:", sin_value)