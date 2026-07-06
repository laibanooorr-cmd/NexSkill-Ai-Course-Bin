# 1.	Unique Words in a Text
# # •	Task: Return a set of unique words from a string (case-insensitive).
import re

def unique_words(text):
    text = text.casefold()
    words = re.findall(r"[a-z]+", text)
    return set(words)
text = input("Enter a sentence: ") #input:  Python is a good language  
result = unique_words(text)
# print("Unique words:", result) #output: Unique words: {'python', 'a', 'language', 'is', 'good'}

# # 1.	Set Operations Demo
# # •	Task: Given two sets A and B, compute union, intersection, difference, symmetric difference.
A = set(map(int, input("Enter elements of Set A: ").split())) #input:  1 2 4 5
B = set(map(int, input("Enter elements of Set B: ").split())) #input: 4 5 6 7

print("\nSet A:", A) #Set A: {1, 2, 4, 5}
print("Set B:", B) #Set B: {4, 5, 6, 7}
print("\nUnion (A | B):", A | B) #Union (A | B): {1, 2, 4, 5, 6, 7}
print("Intersection (A & B):", A & B)#Intersection (A & B): {4, 5}
print("Difference (A - B):", A - B)#Difference (A - B): {1, 2}
print("Symmetric Difference (A ^ B):", A ^ B)#Symmetric Difference (A ^ B): {1, 2, 6, 7}


# 1.	Remove Duplicates from List Using Set
# •	Task: Remove duplicates from a list but don’t preserve order.
numbers = list(map(int, input("Enter numbers separated by spaces: ").split())) # input: 2 3 4 2 5 
unique_numbers = list(set(numbers))
print("Original List:", numbers)#Original List: [ 2, 3, 4, 2, 5]
print("After Removing Duplicates:", unique_numbers)#After Removing Duplicates: [2, 3, 4, 5]


# 1.	Find Missing Numbers
# •	Task: Given a list of ints in 1..n with some missing, return missing numbers.
def find_missing(lst, n):
    full_set = set(range(1, n + 1))
    input_set = set(lst)

    missing = full_set - input_set
    return sorted(missing)
numbers = list(map(int, input("Enter numbers: ").split())) #input: 1 2 3 6 6 
n = int(input("Enter n: "))# input: 6
result = find_missing(numbers, n)
print("Missing numbers:", result)#Missing numbers: [4, 5]

# 1.	Count Items Appearing in All Lists
# •	Task: Given a list of lists, return items that appear in all of them.
def common_items(list_of_lists):
    if not list_of_lists:
        return set()
    common = set(list_of_lists[0])
    for lst in list_of_lists[1:]:
        common &= set(lst)
    return common
n = int(input("How many lists? ")) #input: 3

list_of_lists = []
for i in range(n):
    lst = list(map(int, input(f"Enter elements of list {i+1}: ").split()))#Enter elements of list 1: list 1: 1 2 3, list 2: 2 4 5, list 3: 1 2 5
    list_of_lists.append(lst)
result = common_items(list_of_lists)
print("Common items in all lists:", result)#Common items in all lists: {2}