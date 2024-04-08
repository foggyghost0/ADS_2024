from math import sqrt

"""
Write a program that prints out the message "hello world!" and then asks "shall we continue?"
until the user inputs "no". Then the program should print out "okay then" and finish.

Example:
    hello world!
    shall we continue? >> yes
    hello world!
    shall we continue? >> oui
    hello world!
    shall we continue? >> jawohl
    hello world!
    shall we continue? >> no
    okay then
"""
# while True:
#     print("Hello World!")
#     user_input = input("shall we continue?")
#     if user_input == "no":
#         print("okay then")
#     break

"""
Write a program which asks the user for integer numbers.

- If the number is below zero, the program should print out the message "invalid number".
- If the number is above zero, the program should print out the square root of the number using the Python sqrt function.
- In either case, the program should then ask for another number.
- If the user inputs the number zero, the program should stop asking for numbers and exit the loop.

To use the `sqrt` function in python add the following to the top of your file: 
    from math import sqrt
Then use it like:
    print(sqrt(9))
    
Example:
    Please type in a number: >> 16
    4.0
    Please type in a number: >> 4
    2.0
    Please type in a number: >> -3
    invalid number
    Please type in a number: >> 1
    1.0
    Please type in a number: >> 0
    Exiting...
"""


# while True:
#     number = int(input("Please type in a number: "))
#     if number == 0:
#         print("exiting...")
#         break
#     elif number < 0:
#         print("invalid number")
#     elif number > 0:
#         print(sqrt(number))




"""
This program should print out a countdown. However, the program doesn't quite work. Please fix it.
Hint: you can use the debugger of PyCharm to see how the program is executing.
"""

# number = 5
# print("Countdown!")
# while True:
#     print(number)
#     number -= 1
#     if number < 0:
#         break
# print("Now!")

"""
Write a program which asks the user for a year, and prints out the next leap year.
If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year.

Examples:
    Year: >> 2023
    The next leap year after 2023 is 2024
    
    Year: >> 2024
    The next leap year after 2024 is 2028
"""
# current_year = int(input("Enter a year: "))
# while True:
#     current_year += 1
#     if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
#         print(f"The next leap year after {current_year - 1} is {current_year}.")
#         break

"""
Please write a program which keeps asking the user for words. 
If the user types in end, the program should print out the story the words formed, and finish.

Example:
  Please type in a word: >> Once
  Please type in a word: >> upon
  Please type in a word: >> a
  Please type in a word: >> time
  Please type in a word: >> there
  Please type in a word: >> was
  Please type in a word: >> a
  Please type in a word: >> girl
  Please type in a word: >> end
  Once upon a time there was a girl
"""
# words = []
#
# # Keep asking the user for words until they type "end"
# while True:
#     user_input = input("Please type in a word: >> ")
#     if user_input.lower() == "end":
#         break
#     words.append(user_input)
#
# # Construct the story from the entered words
# if words:
#     story = " ".join(words)
#     print(f"The story formed by the words: {story}")
# else:
#     print("No words entered. The story remains untold.")

"""
Change the program above so that the loop ends also ifhe user types in the same word twice in a row.
"""
# words = []
# previous_word = None
#
# # Keep asking the user for words until they type "end" or repeat the same word
# while True:
#     user_input = input("Please type in a word: >> ")
#     if user_input.lower() == "end":
#         break
#     elif user_input.lower() == previous_word:
#         print("You typed the same word twice. Ending the story.")
#         break
#     words.append(user_input)
#     previous_word = user_input.lower()
#
# # Construct the story from the entered words
# if words:
#     story = " ".join(words)
#     print(f"The story formed by the words: {story}")
# else:
#     print("No words entered. The story remains untold.")

"""
Please write a program which asks the user for integer numbers. 
The program should keep asking for numbers until the user types in 0.

After reading the numbers the program should 
  - print out how many numbers were typed in
  - the sum of numbers entered
  - the mean of numbers entered
  - the number of positive and negative numbers entered
  
Example output
  Numbers typed in 4
  The sum of the numbers is 34
  The mean of the numbers is 8.5
  Positive numbers 3
  Negative numbers 1
"""
numbers = []
positive_count = 0
negative_count = 0
total_sum = 0

# Keep asking the user for numbers until they type 0
# while True:
#     user_input = int(input("Enter an integer (type 0 to stop): "))
#     if user_input == 0:
#           break
#     numbers.append(user_input)
#     total_sum += user_input
#     if user_input > 0:
#         positive_count += 1
#     elif user_input < 0:
#         negative_count += 1
# # Calculate mean
# num_count = len(numbers)
# mean = total_sum / num_count if num_count > 0 else 0
#
# # Display results
# print(f"Numbers entered: {num_count}")
# print(f"Sum of numbers: {total_sum}")
# print(f"Mean of numbers: {mean}")
# print(f"Positive numbers: {positive_count}")
# print(f"Negative numbers: {negative_count}")

"""
Largest Number

Write a program which asks the user for float numbers.
The program should keep asking for numbers until the user types in 0 or a negative number.
The program should then print the largest number.
If the first number entered is less than or equals to 0, the program should quit and print "no number entered".

DO NOT USE LISTS TO SOLVE THIS EXERCISE!

Examples:
  Number 1: >> 3
  Number 2: >> 4.67
  Number 3: >> 120.5
  Number 4: >> 70
  Number 5: >> 0
  The largest number is 120.5
  
  Number 1: >> -1.11
  No number entered.
"""
# largest_number = None
# first_number = None
#
# # Keep asking the user for float numbers until they type 0 or a negative number
# while True:
#     user_input = float(input("Enter a float number (type 0 to stop): "))
#     if user_input <= 0:
#         if first_number is None:
#             print("No number entered.")
#         break
#     if largest_number is None or user_input > largest_number:
#         largest_number = user_input
#     if first_number is None:
#         first_number = user_input
#
# # Print the largest number
# if largest_number is not None:
#     print(f"The largest number entered was: {largest_number}")

"""
Write a program that reads in an integer number (number of lines) and generates the subsequent output using 
two loops on the console (see below). 
If the input of numbers is smaller or equal to 0 an error message should be printed.

Examples:
  n: >> 4
  1
  2 3
  4 5 6
  7 8 9 10
  
  n: >> -1
  Invalid number!
"""
# n = int(input("Enter an integer (number of lines): "))
# if n <= 0:
#     print("Invalid number!")
# else:
#     current_number = 1
#     for i in range(1, n + 1):
#         for j in range(i):
#             print(current_number, end=" ")
#             current_number += 1
#         print()

"""
Write a program that uses loops to create a pyramid of stars '*' on the console. 
The pyramid should have exactly 6 rows.
Example:
       *
      ***
     *****
    *******
   *********
  ***********
"""

# for i in range(1, 7):
#     print(" " * (6 - i) + "*" * (2 * i - 1))

"""
Write a program to calculate the average grade. The console reads in grades between 1 and 5 
until the number 0 is entered. If an invalid grade is entered, an error message is displayed, 
the grade is not counted and the prompt progresses. It is assumed that only integers are entered. 
At the end of the input, the grade average and the number of negatives (grade = 5) are output.

Example:
  Mark 1: >> 5
  Mark 2: >> 3
  Mark 3: >> 10
  Invalid mark!
  Mark 3: >> 1
  Mark 4: >> 5
  Mark 5: >> 0
  Average: 3.50
  Negative marks: 2
"""
# # Initialize variables
# total_grade = 0
# count = 0
# negative_count = 0
# # Keep reading grades until 0 is entered
# while True:
#     try:
#         grade = int(input("Enter a grade (1-5, 0 to stop): "))
#         if grade == 0:
#             break
#         elif 1 <= grade <= 5:
#             total_grade += grade
#             count += 1
#             if grade == 5:
#                 negative_count += 1
#         else:
#             print("Invalid grade. Please enter a grade between 1 and 5.")
#     except ValueError:
#         print("Invalid input. Please enter an integer grade.")
#
# # Calculate average
# if count > 0:
#     average = total_grade / count
#     print(f"Average grade: {average}")
#     print(f"Number of negative grades (grade = 5): {negative_count}")
# else:
#     print("No valid grades entered.")
