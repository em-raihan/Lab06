
def calculator():
    print("=== Python Calculator ===")
    print("Operations: +, -, *, /")
    print("Enter 'c' to clear/reset or 'q' to quit.")

    while True:
        try:
            num1_input = input("Enter first number: ")

            if num1_input.lower() == "q":
                print("Calculator closed.")
                break

            if num1_input.lower() == "c":
                print("Calculator reset successfully!")
                continue

            num1 = float(num1_input)
            operator = input("Enter operator (+, -, *, /): ")

            if operator.lower() == "c":
                print("Calculator reset successfully!")
                continue

            num2 = float(input("Enter second number: "))

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator!")
                continue

            print("Result:", result)

        except ValueError:
            print("Error: Please enter valid numbers.")


if __name__ == "__main__":
    calculator()

