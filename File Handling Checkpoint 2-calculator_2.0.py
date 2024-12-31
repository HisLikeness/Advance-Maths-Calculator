# Create a class called "Calculator" that contains the following:
"""A method called "init" that initializes the dictionary with the basic mathematical operations (+, -, *, /) and corresponding functions"""
import math

class Calculator:

    def __init__(self):
        self.operations = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide
        }
# Use "add_operation" that takes in two arguments: the operation symbol and the corresponding function. This method should add the new operation and function to the dictionary.
    def add(self, first_number, second_number):
        return first_number + second_number

    def subtract(self, first_number, second_number):
        return first_number - second_number

    def multiply(self, first_number, second_number):
        return first_number * second_number

    def divide(self, first_number, second_number):
        if second_number != 0:
            return first_number / second_number
        else:
            return ValueError("Division by zero is not allowed")

# Use "calculate" that takes in three arguments: the first number, the operation symbol, and the second number. This method should use the dictionary to determine the appropriate function to perform the calculation. It should also include error handling to check if the operation symbol is valid and if the input values are numbers. If an error is encountered, the method should print an error message and raise an exception.
    def add_operation(self, symbol, function):
        self.operations[symbol] = function

    def calculate(self, first_number, operation, second_number= None):
        if not isinstance(first_number, (int, float)):
            raise TypeError("First_number must be an integer or float")

        if operation not in self.operations:
            raise ValueError("Invalid Operation")

        if second_number is not None:
            if not isinstance(second_number, (int, float)):
                raise TypeError("Second_number must be an integer or float")
            return self.operations[operation](first_number, second_number)

        return self.operations[operation](first_number)

# Create separate functions for the advanced mathematical operations (exponentiation, square root, logarithm) and use the "add_operation" method to add them to the calculator's dictionary.
def exponential(first_number, second_number):
    return first_number ** second_number

def square_root(first_number):
    if first_number < 0:
        raise ValueError("Cannot compute squart root for negative value")
    return math.sqrt(first_number)

def logrithm(first_number, base = 10):
    if first_number < 0 or base < 0:
        raise ValueError("Logrithm value must be positive base must be greater than zero")
    return math.log(first_number, base)

# In the main program, create an instance of the Calculator class, and use a while loop that allows the user to continue performing calculations until they choose to exit.
calc = Calculator()

calc.add_operation("^", exponential)
calc.add_operation("sqrt", square_root)
calc.add_operation("log", logrithm)

while True:
  try:
        first_input = input(f"\nEnter your first_number (or 'exit' to quit): ").strip().lower()
        if first_input == "exit":
            print("\nExiting calculator")
            break

        first_number = float(first_input)

        operation = input(f"\nEnter the operation (+, -, *, /, ^, sqrt, log): ").strip()

        if operation in ["sqrt", "log"]:
            if operation == "log":
                base = input(f"\nEnter the base for the logrithm  (or press Enter for base 10 ").strip()
                base = float(base) if base else 10
                result = calc.calculate(first_number, "log", base)

            else:
                result = calc.calculate(first_number, "sqrt")

        else:
            second_number = float(input(f"\nEnter your second number:  "))
            result = calc.calculate(first_number, operation, second_number)

        print(f"\nThis is your result: {result}")

  except ValueError as ve:
        print(f"Type Error {ve}")

  except TypeError as te:
        print(f"Type Error {te}")

  except Exception as e:
        print(f"An Error Occured {e}")

  cont = input(f"\nDo you want to perform another calculation? (yes/no): ").strip().lower()
  if cont != "yes":
        print(f"\nExiting Calculator")
        break
