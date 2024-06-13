number = input("Enter a number: ")
sum_of_digits = sum(int(digit) for digit in number if digit.isdigit())
print("The sum of the digits of the given number is:", sum_of_digits)
