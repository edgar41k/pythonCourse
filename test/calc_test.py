def get_user_input():
    num1 = int(input(f"Enther 1st num: "))
    num2 = int(input(f"Enter 2nd num: "))
    operator = input(f"Enther operator: ")
    return num1, num2, operator

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def mod(num1, num2):
    return num1 % num2

def calculator():
    """Perform a calculation based on user input"""
    num1, num2, operator = get_user_input()
    operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
        "%": mod
    }
    if operator in operations:
        result = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {result}")
    else:
        print("Invalid operator!")

def main():
    calculator()

if __name__ == "__main__":
    main()
