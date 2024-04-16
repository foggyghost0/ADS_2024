"""
Exercises "Functions"
"""

"""
### Function Definition / Execution ###

Define a function called "bark()". When executed, "Woof" should get printed to the console.
Execute the function after its definition and run the program!
"""

# def bark():
#     print("Woof")
#
#
# bark()

"""
### Function with 1 Argument, additional logic ###

Write a program that asks the user to enter an animal. The program should respond with the corresponding animal sound.
Define a function called "makeSound(animal)". The function should use the given input to print the correct animal sound.
Add functionality for at least 3 animals and print the right sounds.
If the animal doesn't exists in the program, print "???".
Use a loop to repeatedly ask the user to enter another animal.
Make sure that upper- and lowercase letters both work when entering an animal.

Examples:
    Please enter an animal: >> dog
    Woof
    Please enter an animal: >> Cat
    Meow
    ...
"""

# def make_sound(animal):
#
#     animal = animal.lower()
#
#     if animal == "dog":
#         return "Woof"
#     elif animal == "cat":
#         return "Meow"
#     elif animal == "cow":
#         return "Moo"
#     else:
#         return "???"
#
#
# while True:
#     user_input = input("Please enter an animal: >> ")
#     if user_input.lower() == "exit":
#         print("Exiting...")
#         break
#
#     sound = make_sound(user_input)
#     print(sound)

"""
### Function with 2 Arguments ###

Write a function named print_many_times(text, times), which takes a string and an integer as arguments. 
The integer argument specifies how many times the string argument should be printed out.

Example:
    print_many_times("Gimme Five!", 5)
    Gimme Five!
    Gimme Five!
    Gimme Five!
    Gimme Five!
    Gimme Five!

Additional Task:
Instead of "hard coding", let the user enter the text and the number of times to print it!
Ask the user repeatedly using a loop.
"""

# def print_many_times(text, times):
#     while times > 0:
#         print(text)
#         times -= 1
#
#
# input_str = input("Enter a Word >> ")
# input_number = int(input("Enter a number >> "))
#
# print_many_times(input_str, input_number)

"""
### Return Values ###

Define a function named greatest_number, which takes three arguments. The function returns the greatest in value of the 
three. Use the already defined function "print_greatest" and pass the return value of your function to it!

Example:
 
    
Additional Task:
Add a type hint to the return value of the function!
"""


def greatest_number(a, b, c):
    if a > b and a > c:
        print(f"{a} is the greatest number")
    elif b > a and b > c:
        print(f"{b} is the greatest number")
    else:
        print(f"{c} is the greatest number")


input_a = int(input("Enter a number >> "))
input_b = int(input("Enter a number >> "))
input_c = int(input("Enter a number >> "))

greatest_number(input_a, input_b, input_c)
# def print_greatest(number):
#     print(f"The greatest number is {number}!")


# Write your solution here

"""
### Type Hints ###

Refactor your programs from above and add type hints to all function arguments and return values (if available)!
"""

# No code here, refactor the programs above!

"""
### Named arguments ###

Define a function named super_print which takes two arguments, a string and a boolean value.
If the boolean value is false, print the text as it was. If its True, print it in all upper case.
Use named arguments to use a different order of the arguments. First, use the string as first argument. For the second
call, use the boolean value as the first argument. Also, make use of type hints for the function arguments.

Example Outputs:
    HELLO WORLD
    hello world
"""

# Write your solution here

"""
### Default Values ###

Define a simple function greet() that takes one argument "name". The function should print a greeting for the entered 
name. Ask the user for his/her name and execute the greet function, passing the name as an argument.
If nothing was entered, use a default value for the name to greet "Unknown".

Hint: An empty string is still a value you can pass, be careful :-)

Example:
    Please enter your name: >> René
    Hello René!
    Please enter your name: >> 
    Hello Unknown!
"""

# Write your solution here
