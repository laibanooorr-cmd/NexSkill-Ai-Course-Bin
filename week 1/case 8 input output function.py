# # 1.	Write a program to print "Hello, World!" and your name on two separate lines.
print("Hello, World!") #output: Hello, World!
print("My name is [Laiba Noor]")  #output: My name is Laiba Noor

# # 2.	Ask the user for their favorite color using input() and print "Your favorite color is [color]".
favorite_color = input("Enter your favorite color: ")
print("Your favorite color is:", favorite_color) #output: Your favorite color is: Black

# 3.	Use a single print() statement to display three different words separated by a hyphen (-).
print("copy-book-pencil")  #output: copy-book-pencil

# # 4.	Prompt the user for their birth year and print their age (assume the current year is 2026).
birth_year = int(input("Enter your birth year: ")) #input: 2004
age = 2026 - birth_year
print("Your age is:", age)  #output: Your age is: 22

# 5.	Calculate the result of 5 + 5 and display it in the format: "The sum of 5 and 5 is 10."
result = 5 + 5
print("The sum of 5 and 5 is", result)  #output: The sum of 5 and 5 is 10


# 6.	Use the end parameter in print() to join two separate print statements with a space.
print("Hello, ", end="")
print("World!")  #output: Hello, World!

# # 7.	Write a program that takes two strings from the user and prints them joined together.
string1 = input("Enter the first string: ") #input: programming
string2 = input("Enter the second string: ") #input: language
result = string1 + string2
print("The concatenated string is:", result)  #output: The concatenated string is: programminglanguage

# 8.	Create a greeting that takes a user's name and prints "Welcome, [Name]!" in all uppercase.
name = input("Enter your name: ") #input: Laiba
print("Welcome,", name.upper() + "!")  #output: Welcome, LAIBA!


# 9.	Ask for a user's city and country, then print them in the format: "City, Country".
city = input("Enter your city: ") #input: Lahore
country = input("Enter your country: ") #input: Pakistan
print(city + ", " + country)  #output: Lahore, Pakistan


# 10.	Experiment: What happens if you try to add a string and an integer in a print statement? Write a code snippet that fixes this using str().
number = 15
result = "The number is: "
print(result + str(number))  #output: The number is: 15