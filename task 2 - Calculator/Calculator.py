def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error! Division by zero."


# Dictionary to map choices to functions and names
operations = {
    "1": ("Addition", add),
    "2": ("Subtraction", subtract),
    "3": ("Multiplication", multiply),
    "4": ("Division", divide),
    "5": ("Exit", None)
}


def display_menu():
    print("\n====== Calculator Menu ======")
    for key, (name, _) in operations.items():
        print(f"{key}. {name}")
    print("=============================")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def calculator():
    print("🔢 Welcome to the Python Calculator!")

    while True:
        display_menu()
        choice = input("Select an operation (1-5): ").strip()

        if choice == '5':
            print("👋 Thank you for using the calculator!")
            break

        if choice not in operations:
            print("❌ Invalid choice! Try again.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        op_name, op_func = operations[choice]
        result = op_func(num1, num2)
        print(f"\n✅ Result of {op_name} ({num1} and {num2}): {result}")


if __name__ == "__main__":
    calculator()