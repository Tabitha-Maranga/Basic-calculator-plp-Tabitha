#basic calculator program

print("Welcome to my simple calculator!")

#Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

#perform calculation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        result = "Error! cannot divide by zero."
    else:
        result = num1 / num2
else:
     result = "Invalid operation selected."
#Display result
print(f"\n{num1} {operation} {num2} = {result}")
print("Thank you for using my awesome calculator!")
    

    