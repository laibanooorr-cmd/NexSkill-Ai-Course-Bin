# 21.	Write a program to calculate the area of a rectangle (Length × Width).
length = float(input("Enter the length of the rectangle: ")) #input: 2.5
width = float(input("Enter the width of the rectangle: ")) #input: 3.5
area = length * width   
print("The area of the rectangle is:", area) #output: The area of the rectangle is: 8.75


# 22.	Take two numbers and print the result of the first raised to the power of the second ($a^b$).
a = float(input("Enter the first number: ")) #input: 2.0
b = float(input("Enter the second number: ")) #input: 3.0
result = a ** b
print("The result of", a, "raised to the power of", b, "is:", result) #output: The result of 2.0 raised to the power of 3.0 is: 8.0


# 23.	Demonstrate the difference between / (division) and // (floor division) with the numbers 10 and 3.
num1 = 10
num2 = 3
division = num1 / num2
floor_division = num1 // num2
print("Division (10 / 3):", division) #output: Division (10 / 3): 3.3333333333333335
print("Floor Division (10 // 3):", floor_division) #output: Floor Division (10 // 3): 3

# 24.	Use the modulus operator % to find the remainder when 25 is divided by 4.
remainder = 25 % 4
print("Remainder (25 % 4):", remainder) #output: Remainder (25 % 4): 1

# 25.	Calculate the average of five numbers entered by the user
num1 = float(input("Enter the first number: ")) #input: 2
num2 = float(input("Enter the second number: ")) #input: 4
num3 = float(input("Enter the third number: ")) #input: 6
num4 = float(input("Enter the fourth number: ")) #input: 8
num5 = float(input("Enter the fifth number: ")) #input: 10
average = (num1 + num2 + num3 + num4 + num5) / 5
print("The average of the five numbers is:", average) #output: The average of the five numbers is: 6.0


# 26.	Create a program that converts minutes into hours and remaining minutes.
total_minutes = int(input("Enter the total number of minutes: ")) #input: 130
hours = total_minutes // 60
remaining_minutes = total_minutes % 60
print("Hours:", hours) #output: Hours: 2
print("Remaining Minutes:", remaining_minutes) #output: Remaining Minutes: 10


# 27.	Calculate the area of a circle where $Area = \pi r^2$ (Use $3.14$ for $\pi$).
radius = float(input("Enter the radius of the circle: ")) #input: 5
area = 3.14 * radius ** 2
print("The area of the circle is:", area) #output: The area of the circle is: 78.5

# 28.	Find the cube of a number entered by the user.
number = float(input("Enter a number: ")) #input: 3
cube = number ** 3
print("The cube of", number, "is:", cube) #output: The cube of 3.0 is: 27.0


# 29.	Perform the calculation $10 + 5 * 2$. Does Python follow PEMDAS? Prove it with code.
result = 10 + 5 * 2
print("The result of 10 + 5 * 2 is:", result) #output: The result of 10 + 5 * 2 is: 20


# 30.	Write a program to calculate simple interest: $(P \times R \times T) / 100$.
P = float(input("Enter the principal amount: ")) #input: 1000
R = float(input("Enter the rate of interest: ")) #input: 5
T = float(input("Enter the time in years: ")) #input: 2
simple_interest = (P * R * T) / 100
print("The simple interest is:", simple_interest) #output: The simple interest is: 100.0


