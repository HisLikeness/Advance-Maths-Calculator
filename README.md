# Advance-Maths-Calculator
This project implements a **Calculator** class in Python that supports basic and advanced mathematical operations. It allows users to perform calculations interactively through the command line.

## Features
1. **Basic Operations**:
   - Addition (`+`)
   - Subtraction (`-`)
   - Multiplication (`*`)
   - Division (`/`)

2. **Advanced Operations**:
   - Exponentiation (`^`)
   - Square Root (`sqrt`)
   - Logarithm (`log`)

3. **Extensibility**:
   - Users can add custom operations to the calculator dynamically.

## How It Works
### Class `Calculator`
The `Calculator` class contains:
- `__init__`: Initializes the basic operations dictionary.
- `add_operation(symbol, function)`: Adds a new operation to the dictionary.
- `calculate(first_number, operation, second_number=None)`: Executes the specified operation with error handling.

### Functions for Advanced Operations
- `exponential(first_number, second_number)`: Performs exponentiation.
- `square_root(first_number)`: Computes the square root.
- `logarithm(first_number, base=10)`: Computes the logarithm with a specified base (default is 10).

### Interactive Mode
The program runs in a `while` loop, prompting the user for inputs:
1. Enter the first number (or type `exit` to quit).
2. Select an operation.
3. Enter the second number if required (for binary operations).
4. View the result.

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/calculator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd calculator
   ```
3. Run the program:
   ```bash
   python calculator.py
   ```

## Sample Usage
```plaintext
Enter your first number (or 'exit' to quit): 25
Enter the operation (+, -, *, /, ^, sqrt, log): sqrt

This is your result: 5.0

Do you want to perform another calculation? (yes/no): yes
Enter your first number (or 'exit' to quit): 10
Enter the operation (+, -, *, /, ^, sqrt, log): log
Enter the base for the logarithm (or press Enter for base 10): 

This is your result: 1.0

Do you want to perform another calculation? (yes/no): no
Exiting Calculator
```

## Error Handling
- **Invalid Inputs**: Prompts an error message and asks the user to retry.
- **Division by Zero**: Prevented with a `ValueError`.
- **Invalid Operations**: Raises a `ValueError` for unsupported operations.

## Extending the Calculator
You can add new operations using the `add_operation` method. For example:
```python
def modulus(a, b):
    return a % b

calc.add_operation('%', modulus)
```

## Contributions
Feel free to open issues or submit pull requests for improvements and new features.

---

Enjoy calculating! 😊
```
