'''
Conditional statements:
Conditional statements are used to make decisions in your code — like if something is true, do this, otherwise do something else.
Types of Conditional Statements:
if statement

if...else statement

if...elif...else chain

Nested if statements
'''


# if statement

# age = 18
# if age >= 18:
#     print("you are eligible to vote.")     # If the condition is true, the block runs.


# if else statement

# age = 17
# if age >= 18:
#     print("you are eligible to vote.")
# else:
#     print("you are not eligible to vote.")     # If if is false, else block runs.


#  if...elif...else Chain

# marks = 95

# if marks >= 90:
#     print("Grade A")
# elif marks >=75:
#     print("Grade B")
# elif marks>=50:
#     print("Grade C")
# else:
#     print("Fail")         # Useful when checking multiple conditions.
    


# Nested if Statements 

'''
A nested if statement means putting an if statement inside another if block.
   This is useful when you need to check more than one level of conditions.
   
   Basic Syntax:

if condition1:
    # Outer if block
    if condition2:
        # Inner if block
        # Executes only if both condition1 and condition2 are True
        statement
    else:
        # Executes if condition1 is True but condition2 is False
        statement
else:
    # Executes if condition1 is False
    statement
'''


# num = 10

# if num >0:
#     print("positive number")
#     if num %2:
#         print("even number")
#     else:
#         print("odd number")
# else:
#     print(" negative number")

marks = 0

print(input("Enter Marks: "))


if marks < 0 or marks > 100:
    print("Error: Invalid marks entered")
else:
    if marks < 35:
        print("Fail")
    elif marks >= 35 and marks <= 49:
        print("Pass")
        print("Grade D")
    elif marks >= 50 and marks <= 74:
        print("Grade C")
    elif marks >= 75 and marks <= 89:
        print("Grade B")
    elif marks >= 90 and marks <= 100:
        print("Grade A")
