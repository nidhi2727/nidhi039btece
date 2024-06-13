source_file = input("Enter the path of the source file: ")
destination_file = input("Enter the path of the destination file: ")

with open(source_file, 'r') as source:
    with open(destination_file, 'w') as destination:
        destination.write(source.read())
