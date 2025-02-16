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
