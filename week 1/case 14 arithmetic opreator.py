# 1.	Compute Moving Average (Window k)
# o	Task: Given a list of numbers, compute simple moving average with window k (return list of same length or truncated).
from collections import deque
def moving_average(data, k):
    if k <= 0:
        raise ValueError("Window size k must be greater than 0.")

    if k > len(data):
        return []

    window = deque()
    running_sum = 0
    averages = []

    for num in data:
        window.append(num)
        running_sum += num
        
        if len(window) > k:
            running_sum -= window.popleft()

        
        if len(window) == k:
            averages.append(running_sum / k)

    return averages
numbers = [2, 4, 6, 8, 10, 12]
k = 3
print("Moving Averages:", moving_average(numbers, k)) #output Moving Averages: [4.0, 6.0, 8.0, 10.0]



# 2.	Evaluate Polynomial at x
# o	Task: Given coefficients [a0, a1, ..., an], compute value at x.
def evaluate_polynomial(coefficients, x):
    if not coefficients:
        return 0
    result = 0
    for coeff in reversed(coefficients): 
        result = result * x + coeff
    return result
coefficients = [2, 3, 4]   # 2 + 3x + 4x²
x = 5
print("Polynomial value:", evaluate_polynomial(coefficients, x)) #output Polynomial value: 117


# 3.	GCD/LCM of Multiple Integers
# o	Task: Compute GCD and LCM of a list of integers (positive, nonzero).
import math
from functools import reduce
def gcd_lcm(numbers):
    if not numbers:
        return None, None
    if any(num <= 0 for num in numbers):
        raise ValueError("All numbers must be positive and nonzero.")
    gcd_result = reduce(math.gcd, numbers) # compute gcd
    def lcm(a, b):
        return abs(a * b) // math.gcd(a, b)
    lcm_result = reduce(lcm, numbers) # compute lcm
    return gcd_result, lcm_result
nums = list(map(int, input("Enter numbers separated by spaces: ").split())) #input 50 20 48
gcd_result, lcm_result = gcd_lcm(nums)
print("GCD:", gcd_result) # output: GCD: 2
print("LCM:", lcm_result) # output: LCM: 1200


# 4.	Prime Factorization (Trial Division)
# o	Task: Factorize a positive integer into primes (multiset).
import math

def prime_factorization(n):
    if n < 2:
        return {}
    factors = {}
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    divisor = 3
    while divisor <= math.isqrt(n):
        while n % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            n //= divisor
        divisor += 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors
num = int(input("Enter a positive integer: ")) # input 58

if num < 2:
    print("Number must be greater than or equal to 2.")
else:
    factors = prime_factorization(num)
    print("Prime Factorization:")
    for prime, count in factors.items():
        print(f"{prime}^{count}") #output: Prime Factorization: 2^1, 29^1
        

# 5.	Matrix Addition and Scalar Multiplication
# o	Task: Implement addition of two matrices and scalar multiplication for nested lists.
def is_valid_matrix(matrix):
    """Check if matrix is rectangular (not ragged)."""
    if not matrix:
        return False
    cols = len(matrix[0])
    for row in matrix:
        if len(row) != cols:
            return False
    return True
def add_matrices(A, B):
    """Add two matrices."""
    if not (is_valid_matrix(A) and is_valid_matrix(B)):
        raise ValueError("Invalid (ragged) matrix.")

    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions.")

    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]

def scalar_multiply(matrix, scalar):
    """Multiply a matrix by a scalar."""
    if not is_valid_matrix(matrix):
        raise ValueError("Invalid (ragged) matrix.")
    return [[scalar * element for element in row]
            for row in matrix]
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]
scalar = 3
# Matrix Addition
print("Matrix Addition:") # output Matrix Addition: [6, 8], [10, 12]

result = add_matrices(A, B)
for row in result:
    print(row)
# Scalar Multiplication
print("\nScalar Multiplication:") #output Scalar Multipilication: [3, 6], [9, 12]
result = scalar_multiply(A, scalar)
for row in result:
    print(row)
    
# 6.	Percentage Change and Cumulative Return
# o	Task: Given prices, compute daily percentage changes and cumulativy zero; missing first change.e return.
def percentage_change_and_cumulative_return(prices):
    if len(prices) < 2:
        return [], 0
    changes = []
    cumulative_factor = 1
    for i in range(1, len(prices)):
        if prices[i - 1] == 0:
            raise ValueError("Previous price cannot be zero.")
        change = (prices[i] - prices[i - 1]) / prices[i - 1]
        changes.append(change)
        cumulative_factor *= (1 + change)
    cumulative_return = cumulative_factor - 1
    return changes, cumulative_return
prices = list(map(float, input("Enter prices separated by spaces: ").split()))
daily_changes, cumulative_return = percentage_change_and_cumulative_return(prices)

print("\nDaily Percentage Changes:") #output: Daily Percentage Changes:Day 1: 337.93%, Day 2: -91.34%, Day 3: 100.00%
for i, change in enumerate(daily_changes, start=1):
    print(f"Day {i}: {change:.2%}")

print(f"\nCumulative Return: {cumulative_return:.2%}") #output: Cumulative Return: -24.14%

