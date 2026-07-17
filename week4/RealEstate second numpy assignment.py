import numpy as np

Address,Assessed_Value,Sale_Amount = np.genfromtxt('Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter= ',', usecols = (4, 5, 6), dtype=None, encoding = 'utf-8',skip_header = 1, unpack = True, invalid_raise = False)

print(Address)
print(Assessed_Value)
print(Sale_Amount)


# Zameen.com price  - statistics operations
print("Real-Estate-Second.com - Sale_amount - Average:", np.average(Sale_Amount))
print("Real-Estate-Second.com  - Sale_amount - Median:", np.median(Sale_Amount))
print("Real-Estate-Second.com  - Sale_amount - Mean:", np.mean(Sale_Amount))
print("Real-Estate-Second.com  - Sale_amount - Standard Deviation:", np.std(Sale_Amount))
print("Real-Estate-Second.com  - Sale_amount - percentile - 20:", np.percentile(Sale_Amount, 20))
print("Real-Estate-Second.com  - Sale_amount - percentile - 54:", np.percentile(Sale_Amount, 54))

# calculate max and min
print("Real-Estate-Second.com   - maximum value:", np.max(Sale_Amount))
print("Real-Estate-Second.com   - minimum value:", np.min(Sale_Amount))

# calculate math operation
print("Real-Estate-Second.com  - Sale_amount - square:", np.square(Sale_Amount))
print("Real-Estate-Second.com  - Sale_amount- sqrt:", np.sqrt(Sale_Amount))
print("Real-Estate-Second.com  - Sale_amount - power:", np.pow(Sale_Amount, 2))
print("Real-Estate-Second.com  - Sale_amount - Absolute value:", np.abs(Sale_Amount))

# # calculate arithmetic operations
Addition =  Sale_Amount + Assessed_Value
Subtraction = Sale_Amount- Assessed_Value
Multiplication = Sale_Amount * Assessed_Value
Division = Sale_Amount / Assessed_Value

print("Real-Estate-Second.com  - Addition:", Addition)
print("Real-Estate-Second.com  - Subtraction:", Subtraction)
print("Real-Estate-Second.com  - Multiplication:", Multiplication)
print("Real-Estate-Second.com  - Division:", Division)

# # calculate trignometric functions
Normalized = Sale_Amount/np.max(Sale_Amount)
# # calculate sin
sine = np.sin(Normalized)
print("Real-Estate-Second.com - sine_value:", sine)

# # calculate cosine
cosine = np.cos( Normalized)
print("Real-Estate-Second.com - cosine_value:", cosine)

# # calculate tangent
tangent = np.tan(Normalized)
print("Real-Estate-Second.com - tangent_value:", tangent)
 
# # calculate exponent
print("Real-Estate-Second.com - Exponent:", np.exp(Normalized))
# calculate hyperbolic trignometric functions
# calculate sinh
sinh = np.sinh(Normalized)
print("Real-Estate-Second.com - hyperbolic sinh_value:", sinh)

# # calculate cosh
cosh = np.cosh(Normalized)
print( "Real-Estate-Second.com - hyperbolic cosh_value:", cosh)

# # calculate tanh
tanh = np.tanh(Normalized)
print("Real-Estate-Second.com  - hyperbolic tanh_value:", tanh)

# # calculate inverse hyperbolic functions
# # calculate inverse sinh
asinh = np.arcsinh(Normalized)
print("Real-Estate-Second.com - inverse of sinh_value:", asinh)

# # calculate inverse cosh

acosh = np.arccosh(Sale_Amount)
print("Real-Estate-Second.com  - inverse of cosh_value:", acosh)

# # calculate tanh
Normalized = 2 * (Sale_Amount/np.max(Sale_Amount))
Normalized = np.clip(Normalized, -0.999, 0.999999)
atanh = np.arctanh(Normalized)
print("Real-Estate-Second.com - inverse of tanh_value:", Normalized)

# # calculate Natural log and log10
log_array = np.log(Sale_Amount)
print("Real-Estate-Second.com - Natural log values:", log_array)

log10_array = np.log10(Sale_Amount)
print("Real-Estate-Second.com - Base 10 log values:", log10_array)


# # calculating 2 dimension array
D2SaleAsset = np.array([Sale_Amount,
                         Assessed_Value])
print("Real-Estate-Second.com - 2 dimension array:", D2SaleAsset)

# # check the dimension of array1
print("Real-Estate-Second.com - d dimension array - dimension:", D2SaleAsset.ndim) # output 2

# # return total number of elements in array1
print("Real-Estate-Second.com - d dimension array - total number of element:",D2SaleAsset.size) # output 278

# # return a tuple that gives size of array in each dimension
print("Real-Estate-Second.com - d dimension array - size of array in each dimension:", D2SaleAsset.shape) # output (2, 139)

# # check the data type of array1
print("Real-Estate-Second.com - d dimension array - type of array:",D2SaleAsset.dtype) # output float64

# # slicing of arrys
D2SaleAssetslice = D2SaleAsset[0:1:1, 1:5:1]
print("Real-Estate-Second.com - d dimension array - slicing of array:", D2SaleAssetslice) # output  [[239900. 325000. 202500. 400000.]]
 
D2SaleAssetslice2 = D2SaleAsset[:1, 2:5:4]
print("Real-Estate-Second.com  - d dimension array - slicing of array:", D2SaleAssetslice2) # output   [[325000.]]

# # indexing of array
D2SaleAssetsliceitem = D2SaleAsset[0, 1]
print("Real-Estate-Second.com - d dimension array - indexing of array:", D2SaleAssetsliceitem) # output 239900.0

D2SaleAssetsliceitem2 = D2SaleAsset[0, 2]
print("Real-Estate-Second.com - d dimension array - indexing of array:", D2SaleAssetsliceitem2) # output 325000.0

# #You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer (D2SaleAsset):
    print(elem) 

# #EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate (D2SaleAsset):
    print(elem, index)  
    

# # 2 x 139========>>>>> 1  x 278 
D2LongLat1TO298 = np.reshape(D2SaleAsset, (1, 278))
print("Real-Estate-Second.com - 2 dimentional arrary - np.reshape(D2SaleAsset, (1, 278)) : ", D2LongLat1TO298)
print("Real-Estate-Second.com - 2 dimentional arrary - np.reshape(D2SaleAsset, (1, 278)) : Size " , D2LongLat1TO298.size) #output size 278
print("Real-Estate-Second.com - 2 dimentional arrary - np.reshape(D2SaleAsset, (1, 278)) : ndim " , D2LongLat1TO298.ndim) #output  ndim  2
print("Real-Estate-Second.com - 2 dimentional arrary - np.reshape(D2SaleAsset, (1, 278)) : shape " , D2LongLat1TO298.shape) #output shape  (1, 278)

print()