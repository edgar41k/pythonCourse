num1 = float(input("enter 1st number: "))
num2 = float(input("enter 2nd number: "))
operator = input("enter operator: ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("invalid operator")
    exit()