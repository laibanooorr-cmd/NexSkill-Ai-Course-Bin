#1.	Create a set from [1, 2, 2, 3] and print it.
nums = [1, 2, 2, 3]
num_var = set(nums)
print(num_var) #output {1, 2, 3}


#2.	Add element 4 to the set {1, 2, 3}.
nums = {1, 2, 3}
nums.add(4)
print(nums) #output {1, 2, 3, 4}


#3.	Remove element 2 from the set {1, 2, 3}.
nums = {1, 2, 3}
nums.remove(2)
print(nums) #output {1, 3}


#4.	Check if 5 is in the set {1, 3, 5}.
nums = {1, 3, 5}
print(5 in(nums)) #output True


#5.	Find the length of set {10, 20, 30}.
#Tip: Use len().
nums = {10, 20, 30}
print(len(nums))


#6.	Clear all elements from the set {1, 2, 3}
nums = {1, 2, 3}
nums.clear()
print(nums) #output set()


#7.	Create a set {'a', 'b'} and add 'c' only if it’s missing.
s = {'a', 'b'}
print('c'in(s))
s.add('c')
print(s) #output {'a', 'b', 'c'}


#8.	Convert list ['a', 'a', 'b'] into a set to remove duplicates
s = ['a', 'a', 'b']
nums_set = set(s)
print(nums_set) #output {'a', 'b'}


#9.	Create two sets and print their union
set1 = {1, 2, 3}
set2 = {1, 2, 4}
print("union:",set1|set2) #output  union:{1, 2, 3, 4}


#10.	Create two sets and print their intersection.
#Tip: Use set1 & set2.

set1 = {1, 2, 3, 4}
set2 = {1, 2, 3, 5}
print("intersection:",set1&set2) #ouftput: intersection:{1, 2, 3}


