num1 = float(input("First number: "))
num2 = float(input("Second number: "))
op = input("Operation (+, -, *, /): ")

if op == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif op == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif op == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif op == "/":
    print(f"{num1} / {num2} = {num1 / num2}" if num2 != 0 else "Error: Cannot divide by zero")
else:
    print("Invalid operation")

