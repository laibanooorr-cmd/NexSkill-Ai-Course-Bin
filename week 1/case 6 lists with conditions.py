# 1.	Create a list comprehension that returns the squares of only the even numbers from 0–20.
squares = [x**2 for x in range(21) if x % 2 == 0]
print(squares)

# 2.	Given nums = [3, 1, 4, 1, 5, 9], sort the list without modifying the original.
nums = [3, 1, 4, 1, 5, 9]
result = sorted(nums)
print("sorted list:", result) #output [1, 1, 3, 4, 5, 9]


# 3.	Remove duplicates from a list while preserving the original order.
list = [1, 1, 2, 3, 4, 4,5]
l1 = []
for x in list:
    if x not in l1:
        l1.append(x)
print("li:", l1)  #output [1, 2, 3, 4, 5]      


# 4.	Flatten the nested list [[1, 2], [3, 4], [5]] into a single list 
Nested_list = [[1, 2], [3, 4], [5]]
flat_list = [item for sublist in Nested_list for item in sublist]
print(flat_list) #output [1, 2, 3, 4, 5]


# 5.	Given names = ['alice', 'Bob', 'charlie', 'DAVID'], sort them alphabetically but ignore case
names =  ['alice', 'Bob', 'charlie', 'DAVID']
names.sort(key = str.lower)
print(names) #output ['alice', 'Bob', 'charlie', 'DAVID']


# 6.	Replace items from index 2–4 in a list with [100, 200] using slice assignment.
a = [10, 20, 30, 40, 50, 60, 70]
a[2:5] = [100, 200]
print(a) #output [10, 20, 100, 200, 60, 70]


# 7.	Write a program to find all indices of a value in a list (e.g., all indices of 7).
nums = [7, 2, 7, 4, 7, 9]
target = 7
slice = []
for i, val in enumerate(nums):
    if val == target:
        slice.append(i)
print("indices:", slice) #output indices: [0, 2, 4]


# 8.	Create a new list containing only elements that appear exactly once in the original lis.
nums = [1, 2, 3, 2, 4, 1, 5, 3]
unique_nums = [x for x in nums if nums.count(x) == 1]
print("unique_nums:", unique_nums) #output unique_nums: [4, 5]


# 9.	Rotate a list right by one position (e.g., [1,2,3,4] → [4,1,2,3]).
nums = [1, 2, 3, 4]
rotated =  nums[-1:] + nums[:-1]
print("rotated:", rotated) #output rotated: [4, 1, 2, 3]


# 10.	Split a list into two lists: one with even numbers, one with odd numbers.
nums = [1, 2, 3,4 ,5, 6, 7, 8 ]
even = [x for x in nums if x % 2 ==0]
odd = [x for x in nums if x % 2 != 0]
print("even:", even) #output even: [2, 4, 6, 8]
print("odd:", odd) #output odd: [1, 3, 5, 7]