# 1.	Remove Duplicates but Keep Order
# •	Task: From a list, remove duplicates while preserving first occurrences.
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result
numbers = list(map(int, input("Enter numbers separated by spaces: ").split())) #inputy: 1 2 8 7 8 9 1 2 
unique_numbers = remove_duplicates(numbers)
print("Original List:", numbers) # output : Original List: [1, 2, 8, 7, 8, 9, 1, 2]
print("List after removing duplicates:", unique_numbers) #output: List after removing duplicates: [1, 2, 8, 7, 9]


# 1.	Split List into Chunks of Size n
# •	Task: Split a list into sublists of length n (last may be shorter).
def split_into_chunks(lst, n):
    if n <= 0:
        raise ValueError("Chunk size must be greater than 0.")
    return [lst[i:i+n] for i in range(0, len(lst), n)]
numbers = list(map(int, input("Enter numbers separated by spaces: ").split())) #input 1 2 3 4 5 6 7 
n = int(input("Enter chunk size: ")) #input: 2
try:
    chunks = split_into_chunks(numbers, n)
    print("\nChunks:")
    for chunk in chunks:
        print(chunk) #output: [1, 2], [3, 4], [5, 6], [7]
except ValueError as e:
    print("Error:", e)
    
# 1.	Find Second Largest Unique Number
# •	Task: Given a list of numbers, return the second largest distinct value.
def second_largest(nums):
    unique_nums = set(nums)
    if len(unique_nums) < 2:
        return None
    unique_nums = sorted(unique_nums)
    return unique_nums[-2]
numbers = list(map(int, input("Enter numbers separated by spaces: ").split())) #input: 10 20 30 40 50 
result = second_largest(numbers)
if result is None:
    print("No second largest unique number exists.")
else:
    print("Second largest unique number:", result) #output : Second largest unique number: 40
    
# 1.	Rotate List by k to the Right
# •	Task: Rotate a list right by k positions (return new list).
def rotate_right(lst, k):
    if not lst:
        return []

    k %= len(lst)

    return lst[-k:] + lst[:-k]
numbers = list(map(int, input("Enter numbers separated by spaces: ").split())) # input: 1 2 3 4 5 6 
k = int(input("Enter k: ")) #input: 2
rotated = rotate_right(numbers, k)
print("Original List:", numbers) # output: Original List: [1, 2, 3, 4, 5, 6]
print("Rotated List :", rotated) # output: Rotated List : [5, 6, 1, 2, 3, 4]


# 1.	List Comprehension: Filter and Transform
# •	Task: Given numbers, return squares of even numbers only.
def square_even_numbers(nums):
    return [x * x for x in nums if x % 2 == 0]
numbers = list(map(int, input("Enter numbers separated by spaces: ").split())) # input: 1 5 3 2 4 5 
result = square_even_numbers(numbers)
print("Squares of even numbers:", result) # output: Squares of even numbers: [4, 16]

# 1.	Flatten One Level of Nesting
# •	Task: Flatten a list like [[1,2],[3],[4,5]] to [1,2,3,4,5] (only one level).

def flatten_one_level(lst):
    return [item for sublist in lst for item in sublist]
nested_list = [[1, 2], [3], [4, 5]]
flat_list = flatten_one_level(nested_list)
print("Original List:", nested_list) # output: Original List: [[1, 2], [3], [4, 5]]
print("Flattened List:", flat_list) # output: Flattened List: [1, 2, 3, 4, 5]


# 1.	Element-wise Sum of Two Lists
# •	Task: Given two equal-length lists, compute element-wise sum.
def elementwise_sum(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")
    return [a + b for a, b in zip(list1, list2)]
list1 = list(map(int, input("Enter first list: ").split())) # input: 1 2 3 4 
list2 = list(map(int, input("Enter second list: ").split())) # input:  5 6 7 8
try:
    result = elementwise_sum(list1, list2)
    print("Element-wise Sum:", result) # output: Element-wise Sum: [6, 8, 10, 12]
except ValueError as e:
    print("Error:", e)
    
# 1.	Find Indices of All Occurrences
# •	Task: Return all indices where a target appears in a list.
def find_indices(lst, target):
    return [i for i, value in enumerate(lst) if value == target]
numbers = list(map(int, input("Enter numbers separated by spaces: ").split())) # input: 10 20 50 30 
target = int(input("Enter target value: ")) # input: 50
indices = find_indices(numbers, target)
print("Indices:", indices) # output  Indices: [2]