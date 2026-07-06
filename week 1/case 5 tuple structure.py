#1.	Create a tuple t = (10, 20, 30) and print the second element
tuple = (10, 20, 30)
print(tuple[1]) #output 20

#2.	Find the length of tuple ('a', 'b', 'c')
tuple = ('a', 'b', 'c')
print(len(tuple)) #output 3

#3.	Unpack the tuple (4, 5) into variables x and y
tuple = (4, 5)
x, y = (4, 5)
print(x, y) #output 4, 5


#4.	Check if 'b' is in the tuple ('a', 'b', 'c')
tuple = ('a', 'b', 'c')
print('b' in(tuple)) #output True


#5.	Create an empty tuple and print its type
tuple = ()
print(type( tuple)) #output <class 'tuple'>


#6.	Concatenate (1, 2) and (3, 4) into a new tuple
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print("new tuple:", t3)#output: new tuple:  (1, 2, 3, 4)


#7.	Repeat (7,) three times
tuple = (7,)
t1 = tuple * 3
print("3 times 7:", t1) #output: 3 times 7 (7, 7, 7)


#8.	Find the index of 2 in (1, 2, 3, 2).
#Tip: Use index() method.

number = (1, 2, 3, 2)
result = number.index(2)
print("iondex:", result) #output: index: 1


#9.	Count how many times 2 appears in (1, 2, 3, 2)
number = (1, 2, 3, 2)
result = number.count(2)
print("count:", result) #output: count 2

#10.	Create a single‑element tuple containing the value 5.
result = (5,)
print(result) #output (5,)
print(type(result)) #output <class 'tuple'>