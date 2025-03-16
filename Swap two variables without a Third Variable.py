# Swaping two numbers without using a third variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print(f"After swapping: First number = {a}, Second number = {b}")
