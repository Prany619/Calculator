import math


def add(x, y):
    """Addition"""
    return x + y


def sub(x, y):
    """Subtraction"""
    return x - y


def mul(x, y):
    """Multiplication"""
    return x * y


def div(x, y):
    """Division with zero division check"""
    if y == 0:
        return "Error: Division by zero"
    return x / y


def pow(x, y):
    """Exponentiation"""
    return x ** y


def trig(function, value, unit='degrees'):
    """
    Handles trigonometric functions with error checking
    Supports both regular and inverse functions
    """
    try:
        if function in ['sin', 'cos', 'tan']:
            # Convert to radians if input is in degrees
            angle = math.radians(value) if unit == 'degrees' else value
            if function == 'sin':
                return math.sin(angle)
            elif function == 'cos':
                return math.cos(angle)
            elif function == 'tan':
                if math.cos(angle) == 0:
                    return "Undefined (cos(angle) = 0)"
                return math.tan(angle)

        elif function in ['asin', 'acos', 'atan']:
            # Calculate inverse functions
            result = {
                'asin': math.asin(value),
                'acos': math.acos(value),
                'atan': math.atan(value)
            }[function]
            # Convert to degrees if needed
            return math.degrees(result) if unit == 'degrees' else result

    except ValueError as e:
        return f"Math Error: {str(e)}"
    except KeyError:
        return "Invalid function"


def Calculator():
    """Main calculator interface"""
    print("\n╔══════════════════════════╗")
    print("║      MATH GOD v2.0       ║")
    print("╚══════════════════════════╝")
    print("\nMain Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")
    print("5. Exponentiation (^)")
    print("6. Trigonometric Functions")
    print("Q. Quit")
    print("══════════════════════════")


if __name__ == "__main__":
    while True:
        Calculator()
        choice = input("\nSelect operation (1-6/Q): ").strip().lower()

        if choice == 'q':
            print("\nThank you for using Math God!")
            break

        if choice in ['1', '2', '3', '4', '5']:
            try:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))

                operations = {
                    '1': ('+', add(x, y)),
                    '2': ('-', sub(x, y)),
                    '3': ('×', mul(x, y)),
                    '4': ('÷', div(x, y)),
                    '5': ('^', pow(x, y))
                }
                op_symbol, result = operations[choice]
                print(f"\n{x} {op_symbol} {y} = {result}")

            except ValueError:
                print("Invalid input! Please enter numbers only.")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

        elif choice == '6':
            print("\nTrigonometric Functions:")
            print("1. sin(x)    4. asin(x)")
            print("2. cos(x)    5. acos(x)")
            print("3. tan(x)    6. atan(x)")
            trig_choice = input("\nSelect function (1-6): ").strip()

            if trig_choice in ['1', '2', '3']:
                try:
                    angle = float(input("Enter angle in degrees: "))
                    functions = {'1': 'sin', '2': 'cos', '3': 'tan'}
                    result = trig(functions[trig_choice], angle)
                    print(f"\n{functions[trig_choice]}({angle}°) = {result}")
                except ValueError:
                    print("Invalid input! Please enter a number.")

            elif trig_choice in ['4', '5', '6']:
                try:
                    value = float(input("Enter value: "))
                    functions = {'4': 'asin', '5': 'acos', '6': 'atan'}
                    if trig_choice in ['4', '5'] and not -1 <= value <= 1:
                        print("Error: Value must be between -1 and 1 for asin/acos")
                        continue
                    result = trig(functions[trig_choice], value)
                    print(f"\n{functions[trig_choice]}({value}) = {result}°")
                except ValueError:
                    print("Invalid input! Please enter a number.")

            else:
                print("Invalid choice! Please select 1-6.")

        else:
            print("Invalid operation! Please choose 1-6 or Q.")

        input("\nPress Enter to continue...")