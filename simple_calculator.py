#Program make a simple calculator
####
#****** Function Declaration *********
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

#******* Body ********
while True:
    print("===================")
    print("Select operation.")
    print("0. Exit")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

#Take input from the user
    choice = input("Enter choice(0/1/2/3/4): ")
    if choice == '0' :
        break
    if (choice < '0') or (choice > '4'):
        print("invalid input")
        continue

    num1 = float(input("Enter first number: "))           
    num2 = float(input("Enter second number: "))

    if choice == '1' :
                 print(num1, "+", num2, "=", add(num1, num2))

    if choice == '2' :
                 print(num1, "-", num2, "=", subtract(num1, num2))

    if choice == '3' :
                 print(num1, "*", num2, "=", multiply(num1, num2))

    if choice == '4' :
                 print(num1, "/", num2, "=", divide(num1, num2))
                 
