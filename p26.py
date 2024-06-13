string = input("Enter a string: ")
prefix = input("Enter a prefix to check: ")
suffix = input("Enter a suffix to check: ")

starts_with_prefix = string.startswith(prefix)
ends_with_suffix = string.endswith(suffix)

print("Starts with prefix:", starts_with_prefix)
print("Ends with suffix:", ends_with_suffix)
