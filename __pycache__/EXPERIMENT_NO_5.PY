# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("Error: Division by zero is not allowed")
#     except ValueError:
#         print("Error: Invalid input value")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#     else:
#         print(f"The result of the division is {result}")

# try:
#     # First try block
#     divide(10, 2)  # This will not raise an exception
# except Exception as e:
#     print(f"An exception occurred: {e}")

# try:
#     # Second try block
#     divide(10, 0)  # This will raise a ZeroDivisionError
# except Exception as e:
#     print(f"An exception occurred: {e}")


# try:
#     value = int("string")  # This will raise a ValueError
# except ValueError:
#     print("Invalid conversion to integer.")
# except ZeroDivisionError:
#     print("Division by zero is not allowed.")


with open("input.txt", "r") as file:
    data = file.read()
    print(data)
