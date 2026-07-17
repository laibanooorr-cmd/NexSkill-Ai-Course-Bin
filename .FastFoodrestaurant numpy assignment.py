import numpy as np

address, latitude, longitude, name  = np.genfromtxt('FastFoodRestaurants.csv', delimiter=',',  usecols = (0, 4, 5, 6), dtype = ('U100', 'f8', 'f8', 'U100'), encoding = None, skip_header= 1, invalid_raise = False, unpack = True)

print(address)
print(latitude)
print(longitude)
print(name)


# statistics operations
cleaned_longitude = longitude[~np.isnan(longitude)]
print("FastFoodRestaurant.com longitude - average:", np.average(cleaned_longitude))
print("FastFoodrestaurant.com longitude - median:", np.median(cleaned_longitude))
print("FastFoodRestaurant.com longitude - mean:", np.mean(cleaned_longitude))
print("FastFoodRestaurant.com longitude - std:", np.std(cleaned_longitude))
print("FastFoodRestaurant.com longitude - percentile - 45 :", np.percentile(cleaned_longitude, 45))
print("FastFoodRestaurant.com longitude - percentile - 20:", np.percentile(cleaned_longitude, 20))

# calculate max and min
print("FastFoodRestuarant.com - maximum values:", np.max(cleaned_longitude))
print("FastFoodRestaurant.com - minimum values:", np.min(cleaned_longitude))


# performing trignometric functions
cleaned_longitude = (cleaned_longitude/np.pi) +1

# calculate sine
sin_values = np.sin(cleaned_longitude)
print("FastFoodRestaurant.com - sin_values:", sin_values)

# calculate cosine
cosine_values = np.cos(cleaned_longitude)
print("FastFoodRestaurant.com - cosine_values:", cosine_values)

# calculate tangent
tangent_values = np.tan(cleaned_longitude)
print("FastFoodRestaurant.com - tangent_values:", tangent_values)

# calculate exponent
print("FastFoodRestaurant.com - Exponential values:", np.exp(cleaned_longitude))

# Mathematical functions
print("FastFoodRestaurant.com - longitude - square:", np.square(cleaned_longitude))
print("FastFoodRestaurant.com - longitude - sqrt:", np.sqrt(np.abs(cleaned_longitude)))
print("FastFoodReataurant.com - longitude - pow:", np.power(cleaned_longitude.astype(complex), 0.5))
print("FastFoodRestaurnt.com - longitude - abs:", np.abs(cleaned_longitude))

# Arthematic Operations
Addition = longitude + latitude
Subtraction = longitude - latitude
Multiplication = longitude * latitude
Division = longitude / latitude
print("FastFoodRestaurant.com - lat - Addition:", Addition)
print("FastFoodRestaurant.com - lat - Subtarction:", Subtraction)
print("FastFoodRestaurant.com - lat - Multiplication:", Multiplication)
print("FastFoodRestaurant.com - lat - Division:", Division)


# calculatin log and log10
log_array = np.log(np.abs(cleaned_longitude))
print("FastFoodRestaurant.com - log_array:", log_array)

log10_array = np.log10(np.abs(cleaned_longitude))
print("FastFoodRestaurant.com - log10_array:", log10_array)

# calculate hyperbolic functions
# calculate hyperbolic sinh
sinh_values = np.sinh(cleaned_longitude)
print("FastFoodRestaurant.com - sinh_array:", sinh_values)

# calculate hyperbolic cosh
cosh_array = np.cosh(cleaned_longitude)
print("FastFoodRestaurant.com - cosh_array:", cosh_array)

# calculate hyperbolic tanh
tanh_array = np.tanh(cleaned_longitude)
print("FastFoodRestaurant.com - tanh_array:", tanh_array)

# calculating inverse hyperbolic functions
# calculate inverse hyperbolic sinh
asinh_array = np.arcsinh(cleaned_longitude)
print("FastFoodRestaurant.com - inverse of sinh:", asinh_array) 

# calculate inverse hyperbolic cosh
acosh_array = np.arccosh(np.abs(cleaned_longitude) + 1)
print("FastFoodRestaurant.com - inverse of cosh:",acosh_array)

# calculate inverse hyperbolic tanh
atan_array = np.arctan(cleaned_longitude)
print("FastFoodRestaurant.com - inverse of tanh:", atan_array)

# calculating 2 dimensional arrays
D2longlat = np.array([longitude,
                     latitude])
print("FastFoodRestaurant.com - 2 dimensional array:", D2longlat)

# checking dimension of array 1
print("FastFoodRestaurant.com - 2 dimension array - dimension:", D2longlat.ndim) # output 2

# check return total number of element array 1
print("FastFoodrestaurant.com - 2 dimension array- total numbers of element in array:", D2longlat.size) # output 19980

# return a tuple that gives size of array in each dimension
print("FastFoodRestaurant.com - 2 dimension array - tuple that gives the size of array:", D2longlat.shape) # output (2, 9990)

# check the datatype of array
print("FastFoodRestaurant.com - 2 dimension - datatype of array:", D2longlat.dtype) # output float64


# slicing of arrays
D2longlatslice = D2longlat[1:3:1, 1:2:1]
print("FastFoodRestaurant.com - 2 dimension -slicing of array:", D2longlatslice) # output [[39.53255]]

D2longlatslice2 = D2longlat[1:2, 0:1]
print("FastFoodRestaurant.com - 2 dimension - slicing of array:", D2longlatslice2) # output [[44.9213]]

#indexing of arrays
D2longlatsliceItem = D2longlatslice[0, 0]
print("FastFoodRestaurant.com - 2 dimension - indexing of array:", D2longlatsliceItem) # output 39.53255

D2longlatsliceItem2 = D2longlatslice2[0, 0]
print("FastFoodRestaurant.com - 2 dimension - indexing of array:", D2longlatsliceItem2) # output 44.9213



#You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer (D2longlat):
    print(elem) 
    
#EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate (D2longlat):
    print(elem, index)
    

# 2 x 9990 ========>>>>> 1  x 19980 - reshape
D2LongLat1TO298 = np.reshape(D2longlat, (1, 19980))
print("FastFoodRestaurant.com - 2 dimentional arrary - np.reshape(D2LongLat, (1, 19980)) : ", D2LongLat1TO298)
print("FastFoodRestaurant.com - 2 dimentional arrary - np.reshape(D2LongLat, (1, 19980)) : Size " , D2LongLat1TO298.size) #output size 19980
print("FastFoodRestaurant.com - 2 dimentional arrary - np.reshape(D2LongLat, (1, 19980)) : ndim " , D2LongLat1TO298.ndim) #output  ndim  2
print("FastFoodRestaurant.com - 2 dimentional arrary - np.reshape(D2LongLat, (1, 19980)) : shape " , D2LongLat1TO298.shape) #output shape  (1, 19980)
print("FastFoodRestaurant.com - 2 dimentional arrary - np.reshape(D2LongLat, (1, 19980)) : ndim " , D2LongLat1TO298.ndim) #output ndim  2

print()