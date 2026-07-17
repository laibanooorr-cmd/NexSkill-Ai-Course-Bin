import numpy as np

Startup_Name, Industry, Funding_Rounds, Investment_Amount = np.genfromtxt('startup_growth_investment_data.csv', delimiter = ',', usecols = (0, 1, 2, 3), dtype=('U100','U100',int,float), encoding = None,  skip_header = 1, unpack = True)
print( Startup_Name)
print( Industry)
print( Funding_Rounds)
print( Investment_Amount)


# Zameen.com price  - statistics operations
print("startup_growth_investment_data - Fundin_Rounds - Average:", np.average(Funding_Rounds))
print("startup_growth_investment_data - Fundin_Rounds - Median:", np.median(Funding_Rounds))
print("startup_growth_investment_data - Fundin_Rounds - Mean:", np.mean(Funding_Rounds))
print("startup_growth_investment_data - Fundin_Rounds - Standard Deviation:", np.std(Funding_Rounds))
print("startup_growth_investment_data - Fundin_Rounds - percentile - 20:", np.percentile(Funding_Rounds, 20))
print("startup_growth_investment_data - Fundin_Rounds - percentile - 54:", np.percentile(Funding_Rounds, 54))

# calculate max and min
print("startup_growth_investment_data  - maximum value:", np.max(Funding_Rounds))
print("startup_growth_investment_data  - minimum value:", np.min(Funding_Rounds))

# calculate math operation
print("startup_growth_investment_data - Fundin_Rounds - square:", np.square(Funding_Rounds))
print("startup_growth_investment_data - Fundin_Rounds - sqrt:", np.sqrt(Funding_Rounds))
print("startup_growth_investment_data - Fundin_Rounds - power:", np.pow(Funding_Rounds, Funding_Rounds))
print("startup_growth_investment_data - Fundin_Rounds - Absolute value:", np.abs(Funding_Rounds))

# calculate arithmetic operations
Addition =  Funding_Rounds + Investment_Amount
Subtraction = Funding_Rounds - Investment_Amount
Multiplication = Funding_Rounds * Investment_Amount
Division = Funding_Rounds / Investment_Amount

print("startup_growth_investment_data - Addition:", Addition)
print("startup_growth_investment_data - Subtraction:", Subtraction)
print("startup_growth_investment_data - Multiplication:", Multiplication)
print("startup_growth_investment_data - Division:", Division)

# calculate trignometric functions
# calculate sin
sine = np.sin(Funding_Rounds)
print("startup_growth_investment_data - sine_value:", sine)

# calculate cosine
cosine = np.cos(Funding_Rounds)
print("startup_growth_investment_data - cosine_value:", cosine)

# calculate tangent
tangent = np.tan(Funding_Rounds)
print("startup_growth_investment_data - tangent_value:", tangent)
 
# calculate exponent
print("startup_growth_investment_data - Exponent:", np.exp(Funding_Rounds))
# calculate hyperbolic trignometric functions
# calculate sinh
sinh = np.sinh(Funding_Rounds)
print("startup_growth_investment_data - hyperbolic sinh_value:", sinh)

# calculate cosh
cosh = np.cosh(Funding_Rounds)
print("startup_growth_investment_data - hyperbolic cosh_value:", cosh)

# calculate tanh
tanh = np.tanh(Funding_Rounds)
print("startup_growth_investment_data - hyperbolic tanh_value:", tanh)

# calculate inverse hyperbolic functions
# calculate inverse sinh
asinh = np.arcsinh(Funding_Rounds)
print("startup_growth_investment_data - inverse of sinh_value:", asinh)

# calculate inverse cosh
acosh = np.arccosh(Funding_Rounds)
print("startup_growth_investment_data - inverse of cosh_value:", acosh)

# calculate tanh
Normalized = Funding_Rounds/np.max(Funding_Rounds)
atanh = np.arctanh(Normalized)
print("startup_growth_investment_data - inverse of tanh_value:", Normalized)

# calculate Natural log and log10
log_array = np.log(Funding_Rounds)
print("startup_growth_investment_data - Natural log values:", log_array)

log10_array = np.log10(Funding_Rounds)
print("startup_growth_investment_data - Base 10 log values:", log10_array)


# calculating 2 dimension array
D2FundInvest = np.array([Funding_Rounds,
                         Investment_Amount])
print("startup_growth_investment_data - 2 dimension array:", D2FundInvest)

# check the dimension of array1
print("startup_growth_investment_data - d dimension array - dimension:", D2FundInvest.ndim) # output 2

# return total number of elements in array1
print("startup_growth_investment_data - d dimension array - total number of element:", D2FundInvest.size) # output 10000

# return a tuple that gives size of array in each dimension
print("startup_growth_investment_data - d dimension array - size of array in each dimension:", D2FundInvest.shape) # output (2, 5000)

# check the data type of array1
print("startup_growth_investment_data - d dimension array - type of array:", D2FundInvest.dtype) # output float64

# slicing of arrys
D2FundInvestslice = D2FundInvest[0:1:1, 1:5:1]
print("startup_growth_investment_data - d dimension array - slicing of array:", D2FundInvestslice) # output [[ 2. 10.  5.  9.]]
 
D2FundInvestslice2 = D2FundInvest[:1, 2:5:4]
print("startup_growth_investment_data - d dimension array - slicing of array:", D2FundInvestslice2) # output  [[10.]]

# indexing of array
D2FundInvestsliceitem = D2FundInvest[0, 1]
print("startup_growth_investment_data - d dimension array - indexing of array:", D2FundInvestsliceitem) # output 2.0

D2FundInvestsliceitem2 = D2FundInvest[0, 2]
print("startup_growth_investment_data - d dimension array - indexing of array:", D2FundInvestsliceitem2) # output 10.0

#You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer (D2FundInvest):
    print(elem) 

#EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate (D2FundInvest):
    print(elem, index)  
    

# 2 x 5000========>>>>> 1  x 10000 - reshape
D2LongLat1TO298 = np.reshape(D2FundInvest, (1, 10000))
print("startup_growth_investment_data - 2 dimentional arrary - np.reshape(D2FundInvest, (1, 10000)) : ", D2LongLat1TO298)
print("startup_growth_investment_data - 2 dimentional arrary - np.reshape(D2FundInvest, (1, 10000)) : Size " , D2LongLat1TO298.size) #output size 10000
print("startup_growth_investment_data - 2 dimentional arrary - np.reshape(D2FundInvest, (1, 10000)) : ndim " , D2LongLat1TO298.ndim) #output  ndim  2
print("startup_growth_investment_data - 2 dimentional arrary - np.reshape(D2FundInvest, (1, 10000)) : shape " , D2LongLat1TO298.shape) #output shape  (1, 10000)


print()