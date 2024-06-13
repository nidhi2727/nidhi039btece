numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
minimum_value = min(numbers)
maximum_value = max(numbers)
print("Minimum value in the list:", minimum_value)
print("Maximum value in the list:", maximum_value)
