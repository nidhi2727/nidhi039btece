
numbers = input("Enter a list of numbers separated by spaces: ").split()


element = input("Enter the element to count: ")


count = numbers.count(element)


print(f"The element '{element}' occurs {count} times in the list.")
