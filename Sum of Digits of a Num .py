# Sum all digits of a number
num = input("Enter a number: ")
digit_sum = sum(int(digit) for digit in num)
print(f"Sum of digits: {digit_sum}")
