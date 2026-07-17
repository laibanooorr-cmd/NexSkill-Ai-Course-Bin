import numpy as np

price, bed, bath, acre = np.genfromtxt('RealEstate-USA.csv', delimiter=',', skip_header=1, usecols=(2, 3, 4, 5), dtype=int, encoding=None, unpack=True)

print("price:", price)
print("bed:", bed)
print("bath:", bath)
print("acre:", acre)


print(np.min(price))

# Stastical Operations
print("Real Estate.com price average:", np.average(price))
print("Real Estate.com price mean:", np.mean(price))
print("Real Estate.com price standard deviation:", np.std(price))
print("Real Estate.com price median:", np.median(price))
print("Real Estate.com price percentile - 45:", np.percentile(price,45))
print("Real Estate.com price percentile - 20:", np.percentile(price, 20))

print("Real Estate.com price max:", np.max(price))
print("Real Estate.com price min:", np.min(price))

# math Operations
print("Real Estate.com price square:", np.square(price))
print("Real EState.com price sqrt:", np.sqrt(price))
print("Real Estate.com price pow:", np.pow(price, price))
print("Real Estate.com price abs:", np.abs(price))

#Trignometric Functions
pricepi = (price / np.pi) + 1

#Apply sin, cos and tan

sin_value = np.sin(pricepi)
print("sin:", sin_value)

cos_value = np.cos(price)
print("cos:", cos_value )

tan_value = np.tan(price)
print("tan:", tan_value)

# Basic arithmetic Operations
Addition = bath + acre
Subtraction = bath + acre
Multipilication = bath * acre 
Division = bath / acre

print("Real Estate.com - bath - addition:", Addition)
print("Real Estate.com - bath - subtraction:", Subtraction)
print("Real Estate.com - bath - Multipilication:", Multipilication) 
print("Real Estate.com - bath - division:", Division) 

# calculation of natural and base 10 algorithm
log_array = np.log(pricepi)
print("Real Estate.com, natural algorithm values:", log_array)
log10_array = np.log10(pricepi)
print("Real Estate.com, base 10 algorithm values:", log10_array)



D2bathacre = np.array([bath,
                       acre])
print(D2bathacre)
print(D2bathacre.ndim)
print(D2bathacre.shape)
print(D2bathacre.size)
print(D2bathacre.dtype)

D2bathacreslice = D2bathacre[1:2:1, :4:1]
print(D2bathacreslice)
D2bathacreslice = D2bathacre[2:2:1]
print(D2bathacreslice)

for elem in np.nditer(D2bathacre):
    print(elem)