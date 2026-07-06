# 1.	Swap Two Variables Using Tuples
# •	Task: Swap the values of a and b without a temp variable.
a = int(input("Enter first number (a): ")) #input: 2
b = int(input("Enter second number (b): ")) #input: 5
print("\nBefore Swapping:")
print("a =", a) #output: a = 2
print("b =", b) #output: b = 5
a, b = b, a
print("\nAfter Swapping:")
print("a =", a) #output: a = 5
print("b =", b) #output: b = 2

# 1.	Return Multiple Results from Function
# •	Task: Write a function that returns min, max, and average of a list.
def stats(lst):
    if not lst:
        raise ValueError("List cannot be empty.")

    mn = min(lst)
    mx = max(lst)
    avg = sum(lst) / len(lst)
    return mn, mx, avg   
numbers = list(map(int, input("Enter numbers separated by spaces: ").split())) #input:  10 50 40 30 
try:
    mn, mx, avg = stats(numbers)   

    print("\nMinimum :", mn) #output: Minimum : 10
    print("Maximum :", mx) #output: Maximum : 50
    print("Average :", avg) #output: Average : 32.5
except ValueError as e:
#     print("Error:", e)
    
# 1.	Group Pairs into a Tuple of Tuples
# •	Task: Given flat list [k1, v1, k2, v2, ...], convert to ((k1, v1), (k2, v2), ...).
 def group_pairs(lst):
    if len(lst) % 2 != 0:
        raise ValueError("List length must be even (key-value pairs required).")
    pairs = zip(lst[0::2], lst[1::2])
    return tuple(pairs)
data = input("Enter flat list (space-separated): ").split() #input: a 1 b 2 c 3
result = group_pairs(data)
print("Grouped Tuples:", result) #output: Grouped Tuples: (('a', '1'), ('b', '2'), ('c', '3'))


# 1.	Sort List of Tuples by Second Item
# •	Task: Sort [('a', 3), ('b', 1)] by the number.
def sort_by_second(data):
    return sorted(data, key=lambda t: t[1])
n = int(input("How many tuples? ")) #input: 3

data = []
for _ in range(n):
    item = input("Enter (name value): ").split() #input:  a 3,  b 2, c 1
    data.append((item[0], int(item[1])))
sorted_data = sort_by_second(data)
print("Sorted Tuples:", sorted_data) #output: Sorted Tuples: [('c', 1), ('b', 2), ('a', 3)]

# 1.	Immutable Coordinates with Tuples
# •	Task: Represent 2D points with tuples and compute distances.
import math

p1 = (2, 3)
p2 = (7, 11)
distance = math.hypot(p2[0] - p1[0], p2[1] - p1[1])
print("Point 1:", p1) #output: Point 1: (2, 3)
print("Point 2:", p2) #output: Point 2: (7, 11)
print("Distance:", distance) #output: Distance: 9.433981132056603


