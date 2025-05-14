import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Cannot divide by zero"
    return n1 / n2

divide_op = divide
operation_dict = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(art.logo)
    continue_result = True
    num1 = float(input("First number: "))

    while continue_result:
        for symbol in operation_dict:
            print(symbol)

        operation = input("Pick an operation: ")

        # Check if the operation is valid
        if operation not in operation_dict:
            print(f"Error: '{operation}' is not a valid operation. Please try again.")
            continue
            
        num2 = float(input("Next number: "))

        answer = operation_dict[operation](num1, num2)

        # Check if there was a division by zero error
        if answer == "Error: Cannot divide by zero":
            print(answer)
            # Ask if user wants to start a new calculation
            continue_result = False
            print("\n" * 100)
            calculator()
        else:
            print(f"{num1} {operation} {num2} = {answer}")
            calc2 = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

            if calc2 == "y":
                num1 = answer
            else:
                continue_result = False
                print("\n" * 100)
                calculator()

calculator()