"""
Write a program that asks the user for a number.
The program then determines if the number is even or odd and prints out an appropriate message.

Hint: For checking if the number is even or odd, use the Modulo operator:
remainder = number % 2

Example:

    Enter a number: >> 17
    The number 17 is odd.
"""

# number = int(input("Enter a number "))
# even = number % 2 == 0
# odd = number % 2 != 0
#
# if even:
#     print(f"{number} is even.")
# else:
#     print(f"{number} is odd.")

"""
Write a program that asks the user for their exam grade (as a percentage). 
The program then prints out the following message:

* If the grade is below 50%: "Unfortunately, you failed the exam."
* If the grade is 60% or above: "You passed the exam!"
* If the grade is higher or equal to 90: "You are excellent!"

Example:

    Enter your exam grade: >> 63
    You passed the exam!
"""
# grade = int(input("Please enter your grade percentage "))
#
# if grade <= 50:
#     print("Unfortunately, you failed the exam.")
# elif grade >= 60:
#     print("You passed the exam!")
# if grade >= 90:
#     print("You are excellent!")

"""
Write a program that simulates a simple lunch ordering system. 

1. Ask the user if they want a sandwich, salad, or wrap.
2. If they want a sandwich, ask what kind (chicken, beef, veggie).
3. If they want a salad, ask what dressing (vinaigrette, ranch, caesar).
4. If they want a wrap, ask if they want it toasted.
5. Print a confirmation of their order choice.

Hint: You don't need to verify the user input. But if you want a challenge, try to repeat reading the user input
in case of invalid input. To do so, you might need to research a little bit about "loops" which will be 
covered later in this course :-)

Example:

    Would you like a sandwich, salad, or wrap? >> salad
    What kind of dressing would you like: vinaigrette, ranch, or caesar? >> ranch
    Your order: Salad with ranch dressing
"""

# order = input("Hi! Would you like a sandwich, salad, or wrap? ")
#
# if order == "sandwich":
#     sandwich_kind = input("Would you like it with chicken, beef, or veggie? ")
#     print(f"You have ordered a {order} with {sandwich_kind}")
# elif order == "salad":
#     salad_dressing = input("What dressing would you like? Vinaigrette, ranch or caesar? ")
#     print(f"You have ordered a {order} with {salad_dressing}")
# elif order == "wrap":
#     wrap_type = input("Would you like the wrap toasted? ")
#     if wrap_type == "yes":
#         print(f"You have ordered a {order} that is toasted.")
#     else:
#         print(f"You have ordered a {order} that is not toasted.")
# else:
#     print("Sorry! We dont have that on the menu!")