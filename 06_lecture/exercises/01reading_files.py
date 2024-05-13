"""
The file numbers.txt contains integer numbers, one number per line.

Write a function named largest, which reads the file and returns the largest number in the file.

Notice that the function does not take any arguments. The file you are working with is always named numbers.txt.
"""


def largest():
    with open('numbers.txt', 'r') as file:
        numbers = file.readlines()
        # Convert each line into an integer and find the maximum
        max_number = max(int(number.strip()) for number in numbers)
    return max_number


# Example usage:
print(largest())


"""
The file fruits.csv contains names of fruits, and their prices (see fruits.csv)

Write a function named read_fruits, which reads the file and returns a dictionary based on the contents. 
In the dictionary, the name of the fruit should be the key, and the value should be its price. 
Prices should be of type float.

NB: the function does not take any arguments. The file you are working with is always named fruits.csv.
"""


def read_fruits():
    fruit_prices = {}
    with open('fruits.csv', 'r') as file:
        for line in file:
            fruit_name, price_f = line.strip().split(';')
            fruit_prices[fruit_name] = float(price_f)
    return fruit_prices


fruit_dict = read_fruits()
for fruit, price in fruit_dict.items():
    print(f"{fruit}: ${price:.2f}")


"""
The file matrix.txt contains a matrix (see matrix.csv)

Write two functions, named matrix_sum and matrix_max. 
Both go through the matrix in the file, and then return the sum of the elements or the element with the greatest value, as the names of the functions imply.

Also write the function row_sums, which returns a list containing the sum of each row in the matrix. 
For example, calling row_sums when the matrix in the file is defined as:
    1,2,3
    2,3,4
the function should return the list [6, 9].

Hint: you can also include other helper functions in your program. 
It is very worthwhile to spend a moment considering which functionalities are shared by the three functions you are asked to write. 
Notice that the three functions named above do not take any arguments, but any helper functions you write may take arguments. 
The file you are working with is always named matrix.txt.
"""
# Write your solution here