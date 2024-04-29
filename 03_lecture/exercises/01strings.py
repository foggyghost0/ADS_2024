"""
Write a program which asks the user for a string and an amount.
The program then prints out the string as many times as specified by the amount.
The printout should all be on one line, with no extra spaces or symbols added.

Example:
    Please type in a string: >> hey
    Please type in an amount: >> 4
    heyheyheyhey
"""
# # Get user input for the string
# user_string = input("Enter a string: ")
#
# # Get user input for the amount
# amount_str = int(input("Enter the amount: "))
#
# # Print the string 'amount' times on a single line
# print(user_string * amount_str, end='')


"""
Write a program which asks the user for two strings and then prints out whichever is the longer of the two - 
that is, whichever has the more characters. If the strings are of equal length, the program 
should print out "The strings are equally long".

Examples:

    Please type in string 1: >> hello
    Please type in string 2: >> world
    The strings are equally long
    
    Please type in string 1: >> hey
    Please type in string 2: >> world
    world is longer
"""

# # Get user input for the first string
# string1 = input("Enter the first string: ")
#
# # Get user input for the second string
# string2 = input("Enter the second string: ")
#
# # Compare the lengths of the strings
# if len(string1) > len(string2):
#     print(f"The longer string is: {string1}")
# elif len(string2) > len(string1):
#     print(f"The longer string is: {string2}")
# else:
#     print("The strings are equally long")


"""
Write a program which asks the user for a string. The program then prints out the input string in reversed order, 
from end to beginning. Each character should be on a separate line.
Try to solve this example in 2 ways:
    * once using positive indeces
    * once using negative indeces
"""
# # Get user input for the string
# user_string = input("Enter a string: ")
#
# # Print each character in reverse order (positive indices)
# for character in user_string[::-1]:
#     print(character)

# # Get user input for the string
# user_string = input("Enter a string: ")
#
# # Print each character in reverse order (negative indices)
# for i in range(-1, -len(user_string) - 1, -1):
#     print(user_string[i])

"""
Write a program which asks the user for a string. 
The program then prints out a message based on whether the second character and the second to last character 
are the same or not. See the examples below.

Examples:
    Please type in a string: >> python
    The second and the second to last characters are different
    
    Please type in a string: >> pascal
    The second and the second to last characters are a
"""
# Get user input for the string
# user_string = input("Please type in a string: ")
#
# # Check if the second and second-to-last characters are the same
# if user_string[1] == user_string[-2]:
#     print("The second and the second-to-last characters are the same")
# else:
#     print("The second and the second-to-last characters are different")


"""
Write a program which prints out a line of hash characters, the width of which is chosen by the user.

Examples:
    Width: >> 8
    ########
    
    Width: >> 2
    ##
"""
# Get user input for the width

# width = int(input("Enter the desired width: "))
#
# print("#" * width)


"""
Modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly.

Example:
    Width: >> 10
    Height: >> 3
    ##########
    ##########
    ##########
"""
# width = int(input("Enter the desired width: "))
# height = int(input("Enter the desired height: "))
# for i in range(height):
#     print("#" * width)


"""
 

Examples:
    Please type in a string:hello
    ***************hello
    
    Please type in a string:helloworld
    **********helloworld 
"""
# # Get user input for the string
# user_string = input("Enter a string: ")
#
# # Calculate the number of asterisks needed
# num_asterisks = max(0, 20 - len(user_string))
#
# # Print the result
# print("*" * num_asterisks + user_string)


"""
Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre. 
The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.

If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.

Examples:
    Word: >> testing
    
    ******************************
    *          testing           *
    ******************************

    Word: >> python
    
    ******************************
    *           python           *
    ******************************
"""

# # Get user input for the string
# user_string = input("Enter a string: ")
#
# # Calculate the remaining space for the frame
# remaining_space = 30 - len(user_string)
#
# # Calculate the left and right padding
# left_padding = remaining_space // 2
# right_padding = remaining_space - left_padding
#
# # Print the framed word
# print("*" * 15, user_string.center(30, "*"), "*" * 15, sep="\n")



"""
Write a program which asks the user to type in a string. 
The program then prints out all the substrings which begin with the first character, 
from the shortest to the longest. Have a look at the example below.

Example:
    Please type in a string: >> test
    t
    te
    tes
    test
"""
# # Get user input for the string
# user_string = input("Please type in a string: ")
#
# # Print all substrings starting with the first character
# for i in range(len(user_string)):
#     for j in range(i, len(user_string)):
#         print(user_string[i:j + 1])


"""
Write a program which asks the user to type in a string. 
The program then prints out all the substrings which end with the last character, from the shortest to the longest. 
Have a look at the example below.

Example:
    Please type in a string: >> test
    t
    st
    est
    test
"""
# # Get user input for the string
# user_string = input("Please type in a string: ")
#
# # Print all substrings ending with the last character
# for i in range(len(user_string)):
#     print(user_string[i:])
#
# # Note: This includes the entire string itself as well.


"""
Write a program which asks the user to input a string. The program then prints out different messages if the string 
contains any of the vowels a, e or o.

You may assume the input will be in lowercase entirely. Have a look at the examples below.

    Please type in a string: >> hello there
    a not found
    e found
    o found
    
    Please type in a string: >> hiya
    a found
    e not found
    o not found
"""
# # Get user input for the string
# user_string = input("Please type in a string: ")
#
# # Check if the string contains any of the vowels
# if 'a' in user_string:
#     print("a found")
# else:
#     print("a not found")
#
# if 'e' in user_string:
#     print("e found")
# else:
#     print("e not found")
#
# if 'o' in user_string:
#     print("o found")
# else:
#     print("o not found")



"""
Write a program which asks the user to type in a string and a single character. The program then 
prints the first three character slice which begins with the character specified by the user. 
You may assume the input string is at least three characters long. The program must print out three characters, 
or else nothing.

Pay special attention to when there are less than two characters left in the string after the first occurrence of 
the character looked for. In that case nothing should be printed out, and there should not be any indexing errors 
when executing the program.

Examples:

    Please type in a word: >> mammoth
    Please type in a character: >> m
    mam
    
    Please type in a word: >> banana
    Please type in a character: >> n
    nan
    
    Please type in a word: >> python
    Please type in a character: >> n
"""
# # Get user input for the string
# user_string = input("Please type in a word: ")
#
# # Get user input for the character
# user_char = input("Please type in a character: ")
#
# # Find the index of the specified character
# char_index = user_string.find(user_char)
#
# # Check if the character is found
# if char_index != -1:
#     # Print the first three characters starting from the specified character
#     print(user_string[char_index:char_index + 3])
# else:
#     print("Character not found in the string.")


"""
Write a program which finds the second occurrence of a substring. If there is no second (or first) occurrence, 
the program should print out a message accordingly.

In this exercise the occurrences cannot overlap. For example, in the string aaaa the second occurrence of the 
substring aa is at index 2.

Examples:

    Please type in a string: >> abcabc
    Please type in a substring: >> ab
    The second occurrence of the substring is at index 3.
    
    Please type in a string: >> methodology
    Please type in a substring: >> o
    The second occurrence of the substring is at index 6.
    
    Please type in a string: >> aybabtu
    Please type in a substring: >> ba
    The substring does not occur twice in the string.
"""
# # Get user input for the string
# user_string = input("Please type in a string: ")
#
# # Get user input for the substring
# user_substring = input("Please type in a substring: ")
#
# # Find the index of the first occurrence
# first_occurrence = user_string.find(user_substring)
#
# # Check if the substring appears at least once
# if first_occurrence != -1:
#     # Find the index of the second occurrence, starting after the first
#     second_occurrence = user_string.find(user_substring, first_occurrence + 1)
#     if second_occurrence != -1:
#         print(f"The second occurrence of the substring is at index {second_occurrence}.")
#     else:
#         print("The substring appears only once in the string.")
# else:
#     print("Specified substring not found.")
