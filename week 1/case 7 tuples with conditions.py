# 1.	Convert the list [1, 2, 3, 4] into a tuple and then unpack it into four variables.
list = [1, 2, 3, 4]
t1 = tuple(list)
print("t1:", t1) #ouput t1: (1, 2, 3, 4)
a, b, c, d = t1
print("a, b, c, d:", a, b, c, d) #output a, b, c, d: 1 2 3 4


# 2.	Given t = (('a', 1), ('b', 2), ('c', 3)), create a list of all second elements.
t = (('a', 1), ('b', 2), ('c', 3))
second_element = [x[1] for x in t]
print("second_element:", second_element) #ouput second_element: [1, 2, 3]


# 3.	Write a function that returns multiple values (sum, min, max) using a tuple.
def calculate(number):
    return sum(number), min(number), max(number)
nums = [10, 20, 30 , 40 , 50]
total, minimum, maximum = calculate(nums)
print("sum:", total) #output sum: 150
print("Maximum:", maximum ) #output Maximum: 50
print("Minimum:", minimum ) #output Minimum: 10

# 4.	Combine two tuples (1, 2, 3) and (4, 5) then convert the result to a list
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
combined = tuple1 + tuple2
result = list
print("result:", result) #output result: [1, 2, 3, 4]

# 5.	Given a tuple of numbers, find the element with the highest frequency.
numbers = (1, 2, 3, 2, 4, 2, 5, 3, 2)
max_element = None
max_count = 0
for item in set(numbers):
    count = numbers.count(item)
    if count > max_count:
        max_count = count
        max_element = item
print("Element with highest frequency:", max_element) #ouput Element with highest frequency: 2
print("Frequency:", max_count) #output Frequency: 4

# 6.	Check if two tuples contain the same elements regardless of order
tuple1 = (1, 3, 4)
tuple2 = (3, 4, 1)
result = set(tuple1) == set(tuple2)
print("result:", result) #ouput result: True


# 7.	Extract the last three items from a tuple using slicing.
fruits = ("mango", "orange", "banana", "pear")
result = fruits[-3:]
print("result:", result) #output result: ('orange', 'banana', 'pear')


# 8.	Concatenate a tuple with itself three times (repeat operation).
tuple = (1, 2, 3,)
result = tuple * 3
print("result:", result) #ouput result: (1, 2, 3, 1, 2, 3, 1, 2, 3)


# 9.	Convert a nested tuple ((1,2),(3,4)) into a flat tuple (1,2,3,4).
nested_tuple = ((1, 2), (3, 4))
flat_tuple = ()
for sub in nested_tuple:
    for x in sub:
        flat_tuple += (x,)
print("flat_tuple:", flat_tuple) #ouput flat_tuple: (1, 2, 3, 4)


# 10.	Store coordinates in tuples and calculate the Manhattan distance.
p1 = (2, 3)
p2 = (5, 7)
Manhattan = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
print("Manhattan:", Manhattan) #output Manhattan: 7



# 1.	Given two sets, find elements that are in the first set but not the second.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference = set1 - set2
print("difference:", difference) #output difference: {1, 2}


# 2.	Find common items between three sets using intersection.
s1 = {1, 2, 3}
s2 = {4, 5, 2}
s3 = {1, 2, 6}
intersection = s1 & s2 & s3 
print("intersection:", intersection) #output intersection: {2}



# 3.	Given a sentence, return all unique words in lowercase.
var = ("This is my program")
word = set(var.lower().split())
print("word:", word) #output word: {'is', 'this', 'my', 'program'}


# 4.	Convert a list with duplicates into a set, then back to a sorted list.
list = [1, 5, 3, 5,  2, 4]
result = sorted(set(list))
print("result:", result) #ouput result: [1, 2, 3, 4, 5]



# 5.	Check if one set is a strict subset of another
set1 = {1, 3, 4}
set2 = {1, 4, 3, 5}
result = set1 < set2
print("result:", result) #output result: True


# 6.	Use a set comprehension to collect all squares of numbers from 1–15 that are divisible by 3.
square = {x*x for x in range(1, 16) if x % 3 == 0}
print("square:", square) #output square: {225, 36, 9, 144, 81}


# 7.	Count how many duplicate values exist in a list using sets.
list = [2, 2, 2, 3, 4, 5, 5]
result = (len(list) - len(set(list)))
print("result:", result) #output result: 3



# 8.	Write a program to remove all vowels from a string using a set.
letter = input("Enter a string")
vowels = {'a', 'e', 'i', 'o', 'u', 
          'A', 'E', 'I', 'O', 'U'}
result = " "
for ch in letter:
    if ch not in vowels:
        result += ch
        print("string without vowels:", result) #output string without vowels:  Hll wrld
        

        
#  9.	Find the symmetric difference between two sets.
set1 = {1, 2, 3, 4}
set2 = {1, 2, 5, 6, 7}
result = set1 ^ set2 
print("symmetric_difference:", result) #output symmetric_difference: {3, 4, 5, 6, 7}

# 10.	Check if two strings are anagrams using set comparison (unique characters only).
str1 = input("enter first a string: ")
str2 = input("enter second a stirng: ")

if set(str1.lower()) == set(str2.lower()):
  print("This string have a same unique character")
else:
  print("This string has not a same unique character" ) #output This string has not a same unique character
  

# 1.	Count word frequencies in a sentence and store the results in a dictionary.
sentence = "enter a stringe"
freq = {}
for word in sentence.split():
    freq[word] =  freq.get(word, 0) + 1
    print("freq:", freq) #output freq: {'enter': 1, 'a': 1, 'stringe': 1}

# n2.2.	Invert a dictionary where all values are unique
orignal_dic = {'a':1, 'b':2, 'c':3}
swapped_dic = {}
for key, value in orignal_dic.items():
    swapped_dic[value] = key
    print("orignal_dictionary:", orignal_dic) #output orignal_dictionary: {'a': 1, 'b': 2, 'c': 3}
    print("swapped_dictionary:", swapped_dic) #output swapped_dictionary: {1: 'a', 2: 'b', 3: 'c'}
    

# 3.	Merge two dictionaries where second dictionary overrides first.
dic1 = {'a': 1, 'b': 3}
dic2 = {'c':3, 'd':5}
result = dic1 | dic2
print("result:", result) #output result: {'a': 1, 'b': 3, 'c': 3, 'd': 5}



# 4.	Group words by their first letter into a dictionary of lists.
words = ['apple', 'ant', 'banana', 'ball', 'cat']
grouped = {}
for word in words:
    grouped.setdefault(word[0], []).append(word)
    print(grouped) #output {'a': ['apple', 'ant'], 'b': ['banana', 'ball'], 'c': ['cat']}
    

# 5.	Filter a dictionary to keep only entries with values greater than 50.
marks ={"Ali": 12, 
        "Ahmad": 23, 
        "Asma": 50, 
        "Adil": 60
        }
filtered = {k: v for k, v in marks.items() if v > 50}
print(filtered) #output {'Adil': 60}


# 6.	Given a nested dictionary, safely access a deeply nested key.
History = {
    'user':{
        'profile':{
            'age':29
        }
    }
}
age = History.get('user', {}).get('profile', {}).get('age')
print("age:", age) #output age: 29


# 7.	Write a dictionary comprehension that maps numbers 1–10 to their cubes.
map_number = {x: x**3 for x in range(1, 11)}
print("map_number:", map_number) #output map_number: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}



# 8.	Find the key with the highest value in a dictionary.
d = {'Ali': 45, 'Waseem': 78, 'Amna': 2, 'Aqsa': 90}
data = max(d, key=d.get)
print(data)
print(d[data]) #output Aqsa 90


# 9.	Combine two lists into a dictionary (keys from first list, values from second)
keys = ['name', 'age', 'roll no']
values = ['Ali', 23, 10]
result = dict(zip(keys, values))
print("result:", result) #output result: {'name': 'Ali', 'age': 23, 'roll no': 10}



# 10.	Remove all keys from a dictionary whose values are None.
Data = {'name': 'Ali', 'b': 2, 'c': 23, 'booktitle': 2}
remove_dict = {k: v for k, v in Data.items() if v == 2}
print("remove_dict:", remove_dict) #output remove_dict: {'b': 2, 'booktitle': 2}