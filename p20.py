
numbers = input("Enter a list of numbers separated by spaces: ").split()


numbers = [int(num) for num in numbers]


total = sum(numbers)

print("The sum of the numbers is:", total)
