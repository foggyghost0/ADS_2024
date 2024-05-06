"""
Advanced Exercises, focussing on Lists
"""

"""
### Exercise 1: List Filtering ###

Write a program that initializes a list of integers. Use a loop to fill the list with numbers from 1 to 20.
Then, using list comprehension, create a new list that only includes even numbers from the original list.
Print the original and the filtered lists.

Example Output:
    Original list: [1, 2, 3, ..., 20]
    Filtered list: [2, 4, 6, ..., 20]
"""

# # Initialize an empty list
# original_list = []
#
# # Fill the list with numbers from 1 to 20 using a loop
# for i in range(1, 21):
#     original_list.append(i)
#
# # Create a new list with even numbers using list comprehension
# filtered_list = [x for x in original_list if x % 2 == 0]
#
# # Print the original and filtered lists
# print(f"Original list: {original_list}")
# print(f"Filtered list: {filtered_list}")


"""
### Exercise 2: Todo List Application ###

Create a simple todo list application. Start with an empty list named "todos". 
Allow the user to continuously add new tasks to the list by typing them into the console. 
The user can also type 'done' to stop adding tasks, 'remove' to remove the last task, or 'view' to display all tasks.
Use a loop to handle these inputs and modify the list accordingly. 
If 'done' is typed, print the final list of tasks and exit the loop.

Example Interaction:
    Please enter a task or command: >> Buy milk
    Task added.
    Please enter a task or command: >> Do homework
    Task added.
    Please enter a task or command: >> view
    Current tasks: ['Buy milk', 'Do homework']
    Please enter a task or command: >> remove
    Last task removed.
    Please enter a task or command: >> view
    Current tasks: ['Buy milk']
    Please enter a task or command: >> done
    Final tasks: ['Buy milk']
    Exiting...
"""

# Start with an empty list named "todos"
todos = []

# Use a loop to handle user inputs and modify the list accordingly
# while True:
#     # Ask the user for a task or command
#     command = input("Please enter a task or command: >> ").strip().lower()
#
#     # Check the user input and perform the corresponding action
#     if command == 'done':
#         # Print the final list of tasks and exit the loop
#         print(f"Final tasks: {todos}")
#         print("Exiting...")
#         break
#     elif command == 'remove':
#         # Remove the last task if the list is not empty
#         if todos:
#             todos.pop()
#             print("Last task removed.")
#         else:
#             print("No tasks to remove.")
#     elif command == 'view':
#         # Display all the tasks
#         print(f"Current tasks: {todos}")
#     else:
#         # Add a new task to the list
#         todos.append(command)
#         print("Task added.")


"""
### Exercise 3: Analyzing Numbers ###

Create a program that initializes a list with numbers (you can hard code them or get them from the user).
Write a function that receives this list and returns a new list with the following items:
    - 'max': Maximum value in the list
    - 'min': Minimum value in the list
    - 'average': Average of the numbers
    - 'under_avg': A new list inside the list, containing the numbers from the original list that are below the average
Use loops and conditionals to compute these values and store them in the new list.
Print the list at the end.

Example Input: [1, 2, 3]
Example Output: [3, 1, 2, [1]]

BONUS TASK:
If you want, you can research "dictionaries" in Python and structure your solution like that:
    {
        'max': 3,
        'min': 1,
        'average': 2,
        'under_avg': [1]
    }
"""


# # Function to calculate max, min, average, and numbers under average
# def analyze_numbers(numbers):
#     max_value = max(numbers)
#     min_value = min(numbers)
#     average = sum(numbers) / len(numbers)
#     under_avg = [num for num in numbers if num < average]
#
#     # Return a new list with the computed values
#     return [max_value, min_value, average, under_avg]
#
#
# # Initialize a list with numbers
# numbers_list = [1, 2, 3]  # Example input
#
# # Call the function and store the result
# result = analyze_numbers(numbers_list)
#
# # Print the result
# print(result)

