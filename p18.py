
string1 = input("Enter the first string: ").lower()
string2 = input("Enter the second string: ").lower()


string1 = ''.join(char for char in string1 if char.isalnum())
string2 = ''.join(char for char in string2 if char.isalnum())


if sorted(string1) == sorted(string2):
    print("The strings are anagrams of each other.")
else:
    print("The strings are not anagrams of each other.")
