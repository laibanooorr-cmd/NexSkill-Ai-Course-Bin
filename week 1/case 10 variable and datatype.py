# 11.	Create an integer variable age and a float variable height. Print their types.
age = 25
height = 5.9
print(type(age)) #output: <class 'int'>
print(type(height)) #output: <class 'float'>

# 12.	Store the value $3 + 4j$ in a variable. Print the variable and its type.
complex_num = 3 + 4j
print(complex_num) #output: (3+4j)
print(type(complex_num)) #output: <class 'complex'>

# 13.	Create a boolean variable is_python_fun and set it to True.
is_python_fun = True
print(is_python_fun) #output: True
print(type(is_python_fun)) #output: <class 'bool'>

# 14.	Method 1: Assign three different values to three variables in a single line.
x, y, z = 10, 20, 30
print(x, y, z) #output: 10 20 30

# 15.	Method 2: Assign the same value to three different variables in a single line
a = b = c = 50
print(a, b, c) #output: 50 50 50

# 16.	Take a numeric input from a user and convert it to a float.
user_input = input("Enter a number: ") #input: 42
num = float(user_input)
print(num) #output: the entered number as a float 42.0

# 17.	Take a string input "100" and convert it to an int.
string_input = input("Enter a string number: ") #input: 100
num = int(string_input)
print(num) #output: the entered number as an integer 100


# 18.	Create a variable with a complex number and print only its real part.
complex_num = 3 + 4j
print(complex_num.real) #output: 3.0

# 19.	Define a string variable containing a paragraph and print its length.
paragraph = "python is a high_level programming language."
print(len(paragraph)) #output: 44

# 20.	Swap the values of two variables a and b without using a third variable.
a = 10
b = 20
a, b = b, a
print(a, b) #output: 20 10

