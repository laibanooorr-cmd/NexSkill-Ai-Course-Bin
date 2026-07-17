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
print("Real Estate.com price absolute value:", np.abs(price))
print("Real Estate.com price percentile - 45:", np.percentile(price,45))
print("Real Estate.com price percentile - 20:", np.percentile(price, 20))

print("Real Estate.com price max:", np.max(price))
print("Real Estate.com price min:", np.min(price))

# mathemagtical Operations
print("Real Estate.com price square:", np.square(price))
print("Real EState.com price sqrt:", np.sqrt(price))
print("Real Estate.com price pow:", np.pow(price, price))
print("Real Estate.com price abs:", np.abs(price))


# Basic arithmetic Operations
Addition = bath + acre
Subtraction = bath + acre
Multipilication = bath * acre 
Division = bath / acre

print("Real Estate.com - bath - addition:", Addition)
print("Real Estate.com - bath - subtraction:", Subtraction)
print("Real Estate.com - bath - Multipilication:", Multipilication) 
print("Real Estate.com - bath - division:", Division) 



#Trignometric Functions
pricepi = (price / np.pi) + 1

#Apply sin, cos and tan

sine_value = np.sin(pricepi)
print("Real Estate.com sine_value:", sine_value)

cosine_value = np.cos(price)
print("Real Estate.com cosine_value:", cosine_value )

tan_value = np.tan(price)
print("Real Estate.com tangent_value:", tan_value)


#calculation of natural and base 10 algorithm
log_array = np.log(pricepi)
print("Real Estate.com, natural algorithm values:", log_array)
log10_array = np.log10(pricepi)
print("Real Estate.com, base 10 algorithm values:", log10_array)


# calculate hyperbolic trignometric functions
pricepi2 = price / np.max(np.abs(pricepi))

# calculate hyperbolic sinh
sinh_value = np.sinh(pricepi2)
print("Real Estate.com sinh_value:", sinh_value)

# calculate hyperbolic cosh
cosh_value = np.cosh(pricepi2)
print("Real Estate.com cosh_value:", cosh_value)

# calculate hyperbolic tanh
tanh_value = np.tanh(pricepi2)
print("Real Estate.com tanh_value:", tanh_value)


# calculation of inverse hyperbolic trignomatric functions
# calculate inverse of sinh
asinh_value = np.arcsinh(pricepi)
print("Real Estate.com inverse of asinh_value:", asinh_value)

# calculate the inverse of cosh
acosh_value = np.arccosh(pricepi)
print("Real Estate.com inverse of acosh_value:", acosh_value)

# calculate inverse of tanh
pricepi3 = pricepi / np.max(np.abs(pricepi))
pricepi3 = np.clip(pricepi3, -0.999, 0.999)
atanh_value = np.arctanh(pricepi3)
print("Real Estate.com inverse of atanh_value:", atanh_value)


# calculate 2 Dimension array
D2bathacre = np.array([bath,
                       acre])

print("Real Estate.com - 2 Dimension array:",  D2bathacre) 

# check the dimension of array1
print("Real Estate.com - 2 Dimension array - dimension of array 1:", D2bathacre.ndim) # output 1: 2

# return total number of elements in array1
print("Real Estate.com - 2 Dimension array  - total number of element in array 1:", D2bathacre.shape) # output (2, 200)


# return a tuple that gives size of array in each dimension 
print("Real Estate.com - 2 Dimension array -return tuple that gives the size of array :", D2bathacre.size) # output 400

# check the data type of array1
print("Real Estate.com - 2 Dimension array  - check the data type of array:", D2bathacre.dtype) # output int64


# slicing of array
D2bathacreslice = D2bathacre[1:2:1, :4:1]
print("Real Estate.com - 2 Dimension array  - slicing of array:", D2bathacreslice) # output  [[-1 -1 -1 -1]]
D2bathacreslice2 = D2bathacre[:1, 4:15:4]
print("Real Estate.com - 2 Dimension array  - slicing of array:", D2bathacreslice2) # output  [[2 1 2]]


# indexing of array
D2bathacresliceitem = D2bathacreslice[0, 1]
print("Real Estate.com - 2 Dimension array  - indexing of array:", D2bathacresliceitem) # output -1

D2bathacresliceitem = D2bathacreslice2[0, 2]
print("Real Estate.com - 2 Dimension array  - indexing of array:", D2bathacresliceitem) #output 2



#You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(D2bathacre):
    print(elem)
    
#EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate(D2bathacre):
    print(index, elem)
    

# 2 x 200 ========>>>>> 1  x 400 - reshape
D2LongLat1TO298 = np.reshape(D2bathacre, (1, 400))
print("Real Estate.com - 2 dimentional arrary - np.reshape((D2bathacre, (1, 400)) :" , D2LongLat1TO298)
print("Real Estate.com - 2 dimentional arrary - np.reshape((D2bathacre, (1, 400)): Size : " , D2LongLat1TO298.size) # output Size:  400
print("Real Estate.com - 2 dimentional arrary - np.reshaep((D2bathacre, (1, 400)) : ndim : " , D2LongLat1TO298.ndim) # output  ndim  2
print("Real Estate.com - 2 dimentional arrary - np.reshape((D2bathacre, (1, 400)) : shape: " , D2LongLat1TO298.shape) # output shape  (1, 400)


print()