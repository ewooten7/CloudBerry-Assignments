'''Week 1 Python Fundamentals: Problem-Solving Questions'''


'''Section 1: Syntax & Variables: Understanding Python’s Structure'''

#1 Indentation Error Challenge: The following code has an indentation error. Fix it and explain why indentation matters in Python.

def greet():
    print("Hello, World!") #This needed an indentation. the Colon was key giveaway.
greet()


#2 Variable Assignment & Dynamic Typing: Predict the output and explain how Python dynamically changes types.
x = 10
print(type(x))
x = "Python"
print(type(x))

#3 Mutable vs Immutable: What will the following code output? Explain why lists are mutable but strings are immutable.
name = "Alice"
name[0] = "M"  # Will this work?

#Answer: Error. 'str' object does not support item assignment. Sting CANNOT have reassignable order. A=/=M. IMMUTABLE=UNCHANGING.

numbers = [1, 2, 3]
numbers[0] = 99  # Will this work?
print(numbers)
#Yes, output: [99, 2, 3]. list item 0 (1) is replaced with 99. MUTABLE=CHANGABLE

'SECTION 2: Data Types: Numbers & Operations'

#4. Number Conversion Challenge: Convert an integer to float and then back to integer. Print the type at each step. 
num = 10 #(Hint: Convert num to float and back to int.)

#convert to float
float_num = float(num) 
print("Type of float_num:", type(float_num))

#convert BACK to int
int_num = int(float_num)
print("Type of int_num:", type(int_num))


#5. Arithmetic Operations:
##Write a program that takes two numbers as input and prints:
##Their sum, difference, quotient, and their remainder.
num1 = int(input("Enter the first number: ")) 
num2 = int(input("Enter the second number: ")) 

sum = num1 + num2

difference = num1 - num2

quotient = num1 // num2  

remainder = num1 % num2 

print("Sum:", sum) 

print("Difference:", difference) 

print("Quotient:", quotient) 

print("Remainder:", remainder) 


#6. Complex Number Handling: Create two complex numbers and add them.


'String Manipulation Section'

#7. String Formatting Challenge: Write a function that takes a user’s first name and last name and returns a greeting message using f-strings.
def greet_user(first_name, last_name):
    pass  # Implement function here


#8. String Slicing: Given "PythonProgramming", extract "Python" and "Programming" using slicing.



#9. Palindrome Check: Write a function that checks if a string is a palindrome (e.g., "madam", "racecar").


'Booleans & Logical Operators'

#10. Truthy & Falsy Values: Predict the output:
values = [0, 1, "", "Hello", [], [1,2,3], None]
for v in values:
    if v:
        print(f"{v} is Truthy")
    else:
        print(f"{v} is Falsy")
#Response:



'''SECTION 3: Control Flow (Decisions & Loops)'''

'if-else Statements'
#11. Even or Odd Checker: Write a function that takes an integer and prints "Even" if it’s even and "Odd" otherwise.


#12. Number Categorizer: Given a number, categorize it as negative, zero, or positive using if-else.


'Loops'
#13. Sum of Natural Numbers: Write a program that calculates the sum of all numbers from 1 to N using a for loop.

#14. Factorial Calculation (Loop Method): Compute the factorial of a number using a while loop.

#15. Multiplication Table: Write a program that prints the multiplication table of a number given by the user.

'Loop Control'
#16. Break & Continue Challenge: What will this program output?
for num in range(10):
    if num == 5:
        break
    if num % 2 == 0:
        continue
    print(num)
#Response:

'''SECTION 4: Functions & Scope'''

'Function Basics'
#17. Function to Calculate Square: Write a function square(n) that returns the square of a number.

#18. Function with Default Parameters: Modify the greet_user function to have "Guest" as the default first name.

'Scope Challanges'
#19. Global vs Local Scope: What will be the output of the following?
x = 10
def change_x():
    x = 20
change_x()
print(x)
#Response:

#20. Fixign Scope Issues: Modify the previous function so that it actually modifies x globally.

'''SECTION 5: Error Handling & Debugging'''

'try-except Blocks'
#21. Handling Division Errors: Write a function that safely divides two numbers and handles ZeroDivisionError.


#22. Handling Type Errors: Fix this program using try-except:
num = input("Enter a number: ")
print(num * 2)  # Fix so that it correctly doubles the number

#23. Debugging Challenge: This program has a bug. Fix it.
def add_numbers(a, b):
    return a + c  # There's a mistake here
print(add_numbers(2, 3))



'''🎯 Final Challenge: Mini-Project'''

'Simple Calculator'
# Write a Python program that:
##1. Accepts two numbers from the user.
##2. Asks for an operation (+, -, *, /).
##3. Handles invalid input (e.g., dividing by zero).
##4. Returns the correct result.
