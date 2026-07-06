# Question 1: 
# Write a program that converts a temperature from Celsius to Fahrenheit.
celsius = float(input("Enter temperature in Celsius: ")) #input: 40
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F") #output: 45.0°C is equal to 104.0°F


# Question 2: 
# Calculate Area of a Rectangle 
length = float(input("Enter the length of the rectangle: ")) #input: 4
width = float(input("Enter the width of the rectangle: ")) #input: 5
area = length * width
print(f"The area of the rectangle is: {area}") #output: The area of the rectangle is: 20.0


# Question 3: 
# Calculate Compound Interest 
principal = float(input("Enter the principal amount: ")) #input : 2
rate = float(input("Enter the rate of interest: ")) #input : 5
time = float(input("Enter the time period: ")) #input : 4
CI = principal * (1 + rate/100)**time - principal # Use the formula
print(f"The compound interest is: {CI}") #output: The compound interest is: 0.43101250000000046


# Question 4: 
# Perimeter of a Rectangle - Take length and width as input and calculate the perimeter. 
length = float(input("Enter the length of the rectangle: ")) #input: 2
width = float(input("Enter the width of the rectangle: "))  #input: 4
perimeter = 2 * (length + width)
print(f"The perimeter of the rectangle is: {perimeter}") #output: The perimeter of the rectangle is: 12.0


# Question 5: 
# Average of Three Numbers - Input three numbers and print their average.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
average = (num1 + num2 + num3) / 3
print(f"The average of the three numbers is: {average}") #output: The average of the three numbers is: 2.66


# Question 6: 
# Square and Cube of a Number - Ask the user for a number and display its square and cube
number = float(input("Enter a number: "))
square = number ** 2
cube = number ** 3
print(f"The square of {number} is: {square}") #output: The square of 2.0 is: 4.0
print(f"The cube of {number} is: {cube}") #output: The cube of 2.0 is: 8.0



# Question 7: . 
# Write a program to find: 
# how many candies each student gets 
# how many are left 
candies = int(input("Enter the number of candies: "))
students = int(input("Enter the number of students: ")) 
candies_per_student = candies // students
remaining_candies = candies % students
print(f"Each student gets {candies_per_student} candies.") #output: Each student gets 2 candies.
print(f"Remaining candies: {remaining_candies}") #output: Remaining candies: 0


# Question 8: 
# Calculate Profit or Loss 
cost_price = float(input("Enter the cost price: ")) #input cost price: 10
selling_price = float(input("Enter the selling price: ")) #input selling price: 10
if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f"Profit: {profit}") #output: Profit: 10.0
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print(f"Loss: {loss}") #output: Loss: 10.0
else:
    print("No Profit No Loss") #output: No Profit No Loss



# Question 9: 
# Total Marks and Percentage 
marks = input("Enter marks of 5 subjects separated by space: ") #input: 80 90 70 85 95
marks_list = list(map(float, marks.split()))    
total_marks = sum(marks_list)
percentage = (total_marks / 500) * 100
average = total_marks / 5
print(f"Total marks: {total_marks}") #output: Total marks: 420.0
print(f"Percentage: {percentage:.2f}%") #output: Percentage: 84.00%
print(f"Average: {average}") #output: Average: 84.0


# Question 10: 
# Salary Calculator 
# Input basic salary. Calculate
Basic_salary = float(input("Enter basic salary: ")) # input 2525
HRA = Basic_salary * 0.20 # 20% of basic
DA = Basic_salary * 0.15 # 15% of basic
Total_Salary = Basic_salary + HRA + DA # calculation
print("Total_Salary:", Total_Salary) #output Total_Salary: 3408.75


# Question 11: 
# Age in Months and Days 
# Input your age in years. Calculate and print age in: 
age_in_years = float(input("Enter your age in years: ")) #input: 22
age_in_months = age_in_years * 12
age_in_days = age_in_years * 365
print(f"Your age in months is: {age_in_months}") #output: Your age in months is: 264.0
print(f"Your age in days is: {age_in_days}") #output: Your age in days is: 8030.0


# Question 12: 
# Currency Converter (USD to PKR) 
# Input amount in USD. Convert using a fixed exchange rate.
usd_amount = float(input("Enter amount in USD: ")) #input: 25.5
exchange_rate = 285.0 # Example 
pkr_amount = usd_amount * exchange_rate
print(f"Amount in PKR: {pkr_amount}") #output: Amount in PKR: 7267.5


# Question 13: 
# Sum of First N Natural Numbers  
n = int(input("Enter a number: ")) #input: 5
sum_n = n * (n + 1) / 2
print(f"The sum of first {n} natural numbers is: {sum_n}") #output: The sum of first 5 natural numbers is: 15.0


# Question 14: 
# Input total questions and correct answers, and calculate the percentage score.
total_questions = int(input("Enter total number of questions: ")) #input: 15
correct_answers = int(input("Enter number of correct answers: ")) #input: 10
percentage = (correct_answers / total_questions) * 100
print(f"Percentage of correct answers: {percentage:.2f}%") #output: Percentage of correct answers: 66.67%



# Question 15: 
# Input distance and time, and calculate speed. 
distance = float(input("Enter distance in kilometers: ")) #input: 60
time = float(input("Enter time in hours: ")) #input: 2
speed = distance / time
print(f"Speed: {speed} m/s") #output: Speed: 30.0 m/s


# Question 16: 
# Calculate Body Mass Index (BMI) 
# Input weight (kg) and height (m), then calculate: 
# BMI = weight / (height ** 2)
weight = float(input("Enter weight in kg: ")) #input: 45
height = float(input("Enter height in meters: ")) #input: 12.5
bmi = weight / (height ** 2)
print(f"Body Mass Index (BMI): {bmi:.2f}") #output: Body Mass Index (BMI): 0.29



# Question 17: 
# Convert Minutes to Hours and Minutes 
# Input number of minutes and convert to hours and remaining minutes. 
minutes = int(input("Enter number of minutes: ")) #input: 130
hours = minutes // 60
remaining_minutes = minutes % 60
print(f"{minutes} minutes is equal to {hours} hours and {remaining_minutes} minutes.") #output: 130 minutes is equal to 2 hours and 10 minutes.