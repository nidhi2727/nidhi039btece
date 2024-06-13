import string


input_string = input("Enter a string: ")


cleaned_string = input_string.translate(str.maketrans('', '', string.punctuation))


print("String without punctuation:", cleaned_string)
