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

# Create two complex numbers
complex_num1 = 2 + 3j
complex_num2 = 1 - 2j

# Add the two complex numbers
sum_complex = complex_num1 + complex_num2

# Print the result
print(f"The sum of {complex_num1} and {complex_num2} is: {sum_complex}")


'String Manipulation Section'

#7. String Formatting Challenge: Write a function that takes a user’s first name and last name and returns a greeting message using f-strings.
def greet_user(first_name, last_name):
    pass  # Implement function here
'answer'

def greet_user(first_name, last_name):
    return f"Hello, {first_name} {last_name}! Welcome to Python programming."

# Example Usage
print(greet_user("John", "Doe"))

'Extra: Trimming input for Handling Extra Space'
def greet_user(first_name, last_name):
    first_name = first_name.strip()
    last_name = last_name.strip()
    return f"Hello, {first_name} {last_name}! Welcome to Python programming."

# Example Usage
print(greet_user("  John ", " Doe  "))  # Removes extra spaces

'Empty Input Example'
def greet_user(first_name, last_name):
    if not first_name or not last_name:
        return "Error: Please provide both first and last name."
    return f"Hello, {first_name.strip()} {last_name.strip()}! Welcome to Python."

# Example Usage
print(greet_user("", "Doe"))  # Error message
print(greet_user("Emmanuel", "Doe"))  # Normal greeting




#8. String Slicing: Given "PythonProgramming", extract "Python" and "Programming" using slicing.

'Answer'
text = "PythonProgramming"

# Extract "Python"
first_part = text[:6]  # Slicing from index 0 to 5

# Extract "Programming"
second_part = text[6:]  # Slicing from index 6 to the end

# Print results
print("First part:", first_part)   # Output: Python
print("Second part:", second_part) # Output: Programming

"✔ text[:6] → Starts at index 0, goes up to (but does NOT include) index 6 → Python."
"✔ text[6:] → Starts at index 6, goes until the end of the string → Programming."

'Answer Check: Edge Cases'
def safe_split_string(word, split_index):
    if split_index > len(word) or split_index < 0:
        return "Error: Split index out of range."
    return word[:split_index], word[split_index:]

# Example Usage
print(safe_split_string("CodeMaster", 4))  # ('Code', 'Master')
print(safe_split_string("Short", 10))      # Error message





#9. Palindrome Check: Write a function that checks if a string is a palindrome (e.g., "madam", "racecar").
'Answer 1: Slicing'

def is_palindrome(word):
        word = word.lower() # Convert to lowercase to make it case-insensitive
        return word == word[::-1] # Check if word equals its reverse

#Example
print(is_palindrome("madam"))      # True
print(is_palindrome("racecar"))    # True
print(is_palindrome("Python"))     # False
print(is_palindrome("Level"))      # True (case-insensitive check)

'Answer 2: Using Loops'
def is_palindrome_loop(word): #Defines Function name. Takes ONE Input (word)
    word = word.lower() #Converts the word to lowercase so that case differences don’t affect the check.
    left, right = 0, len(word) - 1
        #left = 0 → Starts at the first character of the word.
        #right = len(word) - 1 → Starts at the last character of the word.
        #Ex: 'racecar'

    while left < right: #Loop runs while left is smaller than right, meaning we haven't checked all letters.
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
            #✔ Moves the left pointer one step forward (left += 1).
            #✔ Moves the right pointer one step backward (right -= 1).
            #✔ Repeats until left and right meet in the middle.



    return True # If no mismatches are found, it means the word is a palindrome, so we return True.

# Example Usage
print(is_palindrome_loop("racecar"))  # True
print(is_palindrome_loop("hello"))    # False

'Errors fixed: wrong equal sign on line 9. Should have been < less than NOT > greater than.'
'Error fixed: wrong def name used.'



'Booleans & Logical Operators'

#10. Truthy & Falsy Values: Predict the output:
values = [0, 1, "", "Hello", [], [1,2,3], None]
for v in values:
    if v:
        print(f"{v} is Truthy")
    else:
        print(f"{v} is Falsy")
#Response:
'Iteration 1: v = 0'
if 0:   # 0 is falsy
    print("0 is Truthy")  
else:
    print("0 is Falsy")

' Iteration 2: v = 1'
if 1:   # 1 is truthy
    print("1 is Truthy")

'Iteration 3: v = "" (Empty String)'
if "":   # Empty string is falsy
    print('"" is Truthy')  
else:
    print('"" is Falsy')

'Iteration 4: v = "Hello" (Non-empty String)'
if "Hello":  # Non-empty strings are truthy
    print("Hello is Truthy")

'Iteration 5: v = [] (Empty List)'
if []:   # Empty list is falsy
    print("[] is Truthy")  
else:
    print("[] is Falsy")

'Iteration 6: v = [1,2,3] (Non-empty List)'
if [1,2,3]:   # Non-empty lists are truthy
    print("[1,2,3] is Truthy")

'Iteration 7: v = None'
if None:   # None is falsy
    print("None is Truthy")  
else:
    print("None is Falsy")

'Final Outputs for everything'
#1) 0 is Falsy.
#2) 1 is Truthy.
#3) "" is Falsy.
#4) Hello is Truthy.
#5) [] is Falsy.
#6) [1,2,3] is Truthy.
#7) None is Falsy.




'''SECTION 3: Control Flow (Decisions & Loops)'''

'if-else Statements'
#11. Even or Odd Checker: Write a function that takes an integer and prints "Even" if it’s even and "Odd" otherwise.

def check_even_odd(number):
    if number % 2 == 0:  # If number is divisible by 2
        print("Even")
    else:
        print("Odd")

# Example Usage
check_even_odd(10)  # Even
check_even_odd(7)   # Odd


#12. Number Categorizer: Given a number, categorize it as negative, zero, or positive using if-else.

def categorize_number(num):
    if num > 0:  
        print("Positive")  # If number is greater than 0
    elif num < 0:
        print("Negative")  # If number is less than 0
    else:
        print("Zero")  # If number is exactly 0

# Example Usage
categorize_number(-5)  # Negative
categorize_number(0)   # Zero
categorize_number(12)  # Positive


'Loops'
#13. Sum of Natural Numbers: Write a program that calculates the sum of all numbers from 1 to N using a for loop.

def sum_natural_numbers(n):
    total = 0
    for i in range(1, n + 1):  # Loop from 1 to N (inclusive)
        total += i  # Add each number to total
    return total

# Example Usage
print(sum_natural_numbers(5))  # Output: 15 (1+2+3+4+5)


#14. Factorial Calculation (Loop Method): Compute the factorial of a number using a while loop.

def factorial(n):
    result = 1
    while n > 0:  # Keep looping while n is greater than 0
        result *= n  # Multiply result by current n
        n -= 1  # Decrease n
    return result

# Example Usage
print(factorial(5))  # Output: 120 (5*4*3*2*1)


#15. Multiplication Table: Write a program that prints the multiplication table of a number given by the user.

def multiplication_table(num):
    for i in range(1, 11):  # Loop from 1 to 10
        print(f"{num} x {i} = {num * i}")  # Print table entry

# Example Usage
multiplication_table(5)


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

def square(n):
    return n * n  # Multiply number by itself

# Example Usage
print(square(4))  # Output: 16


#18. Function with Default Parameters: Modify the greet_user function to have "Guest" as the default first name.

def greet_user(first_name="Guest"):
    return f"Hello, {first_name}!"

# Example Usage
print(greet_user())       # Output: Hello, Guest!
print(greet_user("John")) # Output: Hello, John!


'Scope Challanges'
#19. Global vs Local Scope: What will be the output of the following?
x = 10
def change_x():
    x = 20
change_x()
print(x)

'19. Answer'
x = 10

def change_x():
    x = 20  # This creates a new local variable, doesn't modify global x

change_x()
print(x)  # Output: 10 (Global x remains unchanged)



#20. Fixing Scope Issues: Modify the previous function so that it actually modifies x globally.
'Answer'
x = 10

def change_x():
    global x  # Now we are explicitly modifying the global x
    x = 20

change_x()
print(x)  # Output: 20 (Global x is changed)



'''SECTION 5: Error Handling & Debugging'''

'try-except Blocks'
#21. Handling Division Errors: Write a function that safely divides two numbers and handles ZeroDivisionError.

'21. Answer'
def safe_divide(a, b):
    try:
        result = a / b  # Attempt division
        return result
    except ZeroDivisionError:  # Catch division by zero error
        return "Error: Cannot divide by zero!"

# Example Usage
print(safe_divide(10, 2))  # Output: 5.0
print(safe_divide(5, 0))   # Output: Error: Cannot divide by zero!


#22. Handling Type Errors: Fix this program using try-except:
num = input("Enter a number: ")
print(num * 2)  # Fix so that it correctly doubles the number

'22. Answer'
try:
    num = int(input("Enter a number: "))  # Convert input to integer
    print(num * 2)  # Correctly doubles the number
except ValueError:  # Catch invalid input errors (e.g., letters)
    print("Error: Please enter a valid number!")

#23. Debugging Challenge: This program has a bug. Fix it.
def add_numbers(a, b):
    return a + c  # There's a mistake here
print(add_numbers(2, 3))

'23. Answer'
def add_numbers(a, b):
    return a + c  # There's a mistake here

print(add_numbers(2, 3))  # NameError: 'c' is not defined

'Fixed Code'
def add_numbers(a, b):
    return a + b  # Use 'b' instead of 'c'

# Example Usage
print(add_numbers(2, 3))  # Output: 5


'''🎯 Final Challenge: Mini-Project'''

'Simple Calculator'
# Write a Python program that:
##1. Accepts two numbers from the user.
##2. Asks for an operation (+, -, *, /).
##3. Handles invalid input (e.g., dividing by zero).
##4. Returns the correct result.
