def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


while True:
    print("\n==========")
    print("1. Add")
    print("2. Sub")
    print("3. Mul")
    print("4. Div")
    print("0. Exit")

    ch = int(input("Enter your choice: "))

    match ch:
        case 1:
            a = int(input("Enter First No: "))
            b = int(input("Enter Second No: "))
            print("Result:", add(a, b))

        case 2:
            a = int(input("Enter First No: "))
            b = int(input("Enter Second No: "))
            print("Result:", sub(a, b))

        case 3:
            a = int(input("Enter First No: "))
            b = int(input("Enter Second No: "))
            print("Result:", mul(a, b))

        case 4:
            a = int(input("Enter First No: "))
            b = int(input("Enter Second No: "))
            print("Result:", div(a, b))

        case 0:
            print("Exiting program...")
            break

        case _:
            print("Invalid Choice")
