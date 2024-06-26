"""
Write a function named list_of_stars, which takes a list of integers as its argument.
The function should print out lines of star characters. The numbers in the list specify how many stars each line should contain.

For example, with the function call list_of_stars([3, 7, 1, 1, 2]) the following should be printed out:

    ***
    *******
    *
    *
    **

"""


# def list_of_stars(list1):
#     for i in list1:
#         print(i * "*")
#
#
# mylist = [5, 10, 4, 6, 20]
# list_of_stars(mylist)
#
#
# # or
# def list_of_stars_1(list1):
#     for i in range(0, len(list1)):
#         print(list1[i] * "*")
#
#
# mylist = [5, 10, 4, 6, 20]
# list_of_stars_1(mylist)

"""
Write a function named anagrams, which takes two strings as arguments. 
The function returns True if the strings are anagrams of each other. 
Two words are anagrams if they contain exactly the same characters.

Some examples of how the function should work:

    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False
"""


# def anagrams(str1, str2):
#     # Remove spaces and convert to lowercase
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()
#
#     # Check if the sorted characters of both strings are equal
#     return sorted(str1) == sorted(str2)
#
#
# # Examples of how the function works
# print(anagrams("tame", "meta"))  # True
# print(anagrams("tame", "mate"))  # True
# print(anagrams("tame", "team"))  # True
# print(anagrams("tabby", "batty"))  # False
# print(anagrams("python", "java"))  # False

"""
Write a function named sum_of_positives, which takes a list of integers as its argument. 
The function returns the sum of the positive values in the list.

    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result) # prints The result is 9

"""
# def sum_of_positives(numbers):
#     # Use list comprehension to filter out positive numbers and sum them
#     return sum(x for x in numbers if x > 0)
#
# # Example usage
# my_list = [1, -2, 3, -4, 5]
# result = sum_of_positives(my_list)
# print("The result is", result)  # This will print: The result is 9



"""
Write a function named even_numbers, which takes a list of integers as an argument. 
The function returns a new list containing the even numbers from the original list.

    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)
    
    Prints:
        original [1, 2, 3, 4, 5]
        new [2, 4]
"""
def even_numbers(numbers):
    """
    Returns a new list containing even numbers from the input list.
    """
    return [num for num in numbers if num % 2 == 0]

# Example usage
my_list = [1, 2, 3, 4, 5]
new_list = even_numbers(my_list)

print("original", my_list)
print("new", new_list)



"""
Write a function named list_sum which takes two lists of integers as arguments. 
The function returns a new list which contains the sums of the items at each index in the two original lists. 
You may assume both lists have the same number of items.

An example of the function at work:

    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]
"""
def list_sum(list1, list2):
    """
    Returns a new list with the sums of the corresponding items of the two input lists.
    """
    return [x + y for x, y in zip(list1, list2)]

# Example usage
a = [1, 2, 3]
b = [7, 8, 9]
print(list_sum(a, b))  # Output: [8, 10, 12]

