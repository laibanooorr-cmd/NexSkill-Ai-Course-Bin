# 31.	Compare two numbers entered by the user and print if the first is greater than the second.
num1 = float(input("Enter the first number: ")) #input: 10
num2 = float(input("Enter the second number: ")) #input: 5
if num1 > num2:
    print(num1, "is greater than", num2) #output: 10.0 is greater than 5.0
   

# 32.	Check if a user-entered number is even (Number % 2 == 0) and print the Boolean result
number = float(input("Enter a number: ")) #input: 10
is_even = number % 2 == 0
print("Is the number even?", is_even) #output: Is the number even? True


# 33.	Write a program that checks if a number is between 10 and 50 (inclusive) using and.
number = float(input("Enter a number: ")) #input: 25
is_between = number >= 10 and number <= 50
print("Is the number between 10 and 50?", is_between) #output: Is the number between 10 and 50? True



# 34.	Check if a string entered by the user is equal to "Python".
user_string = input("Enter a string: ") #input: "Python"
is_equal = user_string == "Python"
print("Is the string equal to 'Python'?", is_equal) #output: Is the string equal to 'Python'? True


# 35.	Use the or operator to check if a user is either "Admin" or "Superuser".
user_role = input("Enter your role: ") #input: "Admin"
is_admin_or_superuser = user_role == "Admin" or user_role == "Superuser"
print("Is the user either 'Admin' or 'Superuser'?", is_admin_or_superuser) #output: Is the user either 'Admin' or 'Superuser'? True


# 36.	Demonstrate the not operator by reversing a Boolean variable.
is_true = True
is_false = not is_true
print("Is the variable true?", is_true) #output: Is the variable true? True
print("Is the variable false?", is_false) #output: Is the variable false? False


# 37.	Compare two floating-point numbers: 0.1 + 0.2 == 0.3. Explain the result.
result = (0.1 + 0.2) == 0.3
print("0.1 + 0.2 == 0.3", result) #output 0.1 + 0.2 == 0.3 False


# 38.	Take a user's age and check if they are NOT under 18.
age = int(input("Enter your age:")) #input 18
not_under_eighteen = age >= 18
print(not_under_eighteen) #output Enter your age:18 True



# 39.	Check if a number is positive and odd using logical operators.
number = int(input("Enter a number: ")) #input 5
is_positive_and_odd = number > 0 and number % 2 != 0
print("Is the number positive and odd?", is_positive_and_odd) #output: Is the number positive and odd? True


#   40.	Compare the lengths of two strings provided by the user.
string1 = input("Enter the first string: ") #input: "Hello"
string2 = input("Enter the second string: ") #input: "World"
lengths_equal = len(string1) == len(string2)
print("Are the lengths of the strings equal?", lengths_equal) #output: Are the lengths of the strings equal? True   