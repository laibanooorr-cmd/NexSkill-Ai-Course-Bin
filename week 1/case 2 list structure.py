#1.	Create a list 
nums = [3, 1, 4, 1, 5]
print(nums[0])# output 3
print(nums[-1])# output 5

#2. Find the length 
colors = ['red', 'blue', 'green']
print(len(colors))# output 3, 5, 3

#3. Append 'yellow' to the list 
colors = ['red', 'blue']
colors.append('yellow')
print( colors) #output ['red', 'blue', 'yellow']

#4. insert 'orange' at index 1 in fruits = ['apple', 'banana']
fruits = ['apple', 'banana']
fruits.insert(1, 'orange')
print(fruits) #output ['apple', 'orange', 'banana']

#5. Remove 'banana' from fruits = ['apple', 'banana', 'grapes']
fruits = ['apple', 'banana', 'grapes']
fruits.remove('banana')
print(fruits) #output ['apple', 'grapes']

#6.	Pop the last element from items = [10, 20, 30] 
items = [10, 20, 30]
items.pop(2)
print(items) #ouput [10, 20]

#7.	Check if 3 is in the list nums = [1, 2, 3, 4]
nums = [1, 2, 3, 4]
print(3 in(nums)) #output True

#8.	Print the slice [2, 3] from the list [0, 1, 2, 3, 4]
list = [0, 1, 2, 3, 4,]
print(list[2:4]) #output [2, 3]

#9.	Replace the element at index 1 in a = [5, 10, 15] with 12
a = [5, 10, 15]
a[1] = 12 #index 1
print(a) #output [5, 12, 15]

#10.	Count how many times 2 appears in [1, 2, 2, 3, 2].
list = [1, 2, 2, 3, 2]
x = list.count(2)
print(x) #output 3


