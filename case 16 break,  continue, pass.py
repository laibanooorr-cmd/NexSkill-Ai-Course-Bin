# # #1.	Search for First Even in Nested Lists
# # #•	Task: Given a nested list of ints, find the first even and stop scanning as soon as found.
# # def first_even(nested):
# #     for sublist in nested:
# #         for num in sublist:
# #             if num % 2 == 0:
# #                 return num  
# #     return None
# # data = [[1, 3, 5], [7, 9], [11, 12, 13]]

# # result = first_even(data)
# # print("First even:", result) # output: First even: 12


# # # 1.	Filter Lines: Skip Comments and Empty
# # # •	Task: From a list of strings, return lines that are not empty and don’t start with #.
# # def filter_lines(lines):
# #     result = []

# #     for line in lines:
# #         if line.strip() == "":
# #             continue 

# #         if line.lstrip().startswith("#"):
# #             continue  

# #         result.append(line)

# #     return result
# # data = [
# #     "print('Hello')",
# #     "",
# #     "   ",
# #     "# this is a comment",
# #     "   # indented comment",
# #     "x = 10",
# #     "y = 20"
# # ]

# # filtered = filter_lines(data)
# # print("Filtered Lines:")
# # for line in filtered:
# #     print(repr(line)) # output: Filtered Lines: "print('Hello')", 'x = 10', 'y = 20'
    

# # # 1.	Sum Until Sentinel with Early Break
# # # •	Task: Sum input numbers until encountering a sentinel value (e.g., -999), then stop.
# # def sum_until_sentinel(numbers, sentinel=-999):
# #     total = 0
# #     found = False
# #     for num in numbers:
# #         if num == sentinel:
# #             found = True
# #             break
# #         total += num

# #     return total, found
# # data = list(map(int, input("Enter numbers separated by space: ").split())) # input 10 20 30 -999 50 60

# # result, stopped = sum_until_sentinel(data)

# # print("\nSum:", result) # output: Sum: 60

# # if stopped:
# #     print("Stopped due to sentinel.") # output: Stopped due to sentinel.
# # else:
# #     print("No sentinel found.")
    

# # # 1.	Validate Tokens; Skip Invalid
# # # •	Task: Parse space-separated tokens; keep integers, skip the rest, and compute their sum.
# # # •	Dev tip: Split, attempt int(tok) inside try/except ValueError; continue on failure. Track invalid count for reporting.
# # def validate_and_sum(tokens):
# #     total = 0
# #     invalid_count = 0
# #     valid_numbers = []

# #     for tok in tokens:
# #         try:
# #             num = int(tok)   
# #             total += num
# #             valid_numbers.append(num)
# #         except ValueError:
# #             invalid_count += 1
# #             continue

# #     return total, invalid_count, valid_numbers
# # data = input("Enter space-separated tokens: ").split() # input: 10 50 $ bca 20   
# # total, invalid, valid_list = validate_and_sum(data)
# # print("\nValid numbers:", valid_list) # output: Valid numbers: [10, 50, 20]
# # print("Sum:", total)  #output: Sum: 80
# # print("Invalid tokens:", invalid) #output: Invalid tokens: 2


# # 1.	Placeholder Branch with pass
# # •	Task: Build a menu loop with options where unimplemented choices use pass and show a “coming soon” message.
# while True:
#     print("\n=== MENU ===")
#     print("1. Say Hello") # output: 1. Say Hello
#     print("2. Add Numbers (Coming soon)") # output: 2. Add Numbers (Coming soon)
#     print("3. Multiply Numbers (Coming soon)") # output: 3. Multiply Numbers (Coming soon)
#     print("4. Exit") # output: 4. Exit

#     choice = input("Enter your choice: ") # input: 2
#     if choice == "1":
#         name = input("Enter your name: ")
#         print(f"Hello, {name}!")
#     elif choice == "2":
#         print("Add Numbers feature coming soon!") # output: Add Numbers feature coming soon!
#         pass
#     elif choice == "3":
#         print("Multiply Numbers feature coming soon!")
#         pass
#     elif choice == "4":
#         print("Exiting program...")
#         break
#     else:
#         print("Invalid choice. Try again.")
        

# 1.	Retry Fixed Attempts
# •	Task: Try an operation up to 3 times; on success, break; otherwise report failure after loop.
import random

def risky_operation():
    """
    Simulated operation:
    50% chance of success
    """
    return random.choice([True, False])


max_tries = 3

for attempt in range(1, max_tries + 1):
    print(f"Attempt {attempt}...") # output: Attempt 1...  Success! Operation completed.

    if risky_operation():
        print("Success! Operation completed.") 
        break
    else:
        print("Failed attempt.")

else:
    print("All retries failed. Operation unsuccessful.") 
    

    

