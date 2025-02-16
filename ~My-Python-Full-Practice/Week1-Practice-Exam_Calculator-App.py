"""📌 Simple Calculator App (Using Only Week 1 Concepts)
# ✅ Goal: Build a text-based calculator in Python using only concepts from Week 1.

# 📌 Concepts Used (From Week 1)
# ✔ Variables & Data Types → Store numbers & operations.
# ✔ Control Flow (if-else) → Choose the correct operation.
# ✔ Loops (while True) → Keep the calculator running.
# ✔ Error Handling (try-except) → Handle invalid inputs & division by zero.
# ✔ Functions (def) → Organize reusable code.
# ✔ User Input (input()) → Get values from the user."""


def calculate(num1, num2, operation):
    """Performs the selected operation on two numbers."""
    try:
        num1, num2 = float(num1), float(num2)  # Convert input to float
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            if num2 == 0:
                return "Error: Cannot divide by zero!"
            return num1 / num2
        else:
            return "Invalid operation!"
    except ValueError:  # Handle non-numeric input
        return "Error: Please enter valid numbers!"

# Main loop for user interaction
while True:
    print("\n--- Simple Calculator ---")
    
    # Get user input
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    operation = input("Choose operation (+, -, *, /): ")

    # Perform calculation
    result = calculate(num1, num2, operation)

    # Display result
    print("Result:", result)

    # Ask if user wants to continue
    again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if again != "yes":
        print("Goodbye!")
        break  # Exit loop if user enters anything other than "yes"

