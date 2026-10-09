def add_numbers(num1, num2):
    return num1 + num2


def subtract_numbers(num1, num2):
    return num1 - num2


def multiply_numbers(num1, num2):
    return num1 * num2


def divide_numbers(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero."
    return num1 / num2

print("Modular Calculator")

first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))

   
print("\nChoose operation:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

choice = input("\nEnter choice (1-4): ")

    
if choice == "1":
    result = add_numbers(first_num, second_num)
elif choice == "2":
    result = subtract_numbers(first_num, second_num)
elif choice == "3":
    result = multiply_numbers(first_num, second_num)
elif choice == "4":
    result = divide_numbers(first_num, second_num)
else:
    result = "Invalid. Enter a number from 1 to 4."

   
print(f"\nResult: {result}")


