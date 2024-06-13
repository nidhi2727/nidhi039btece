lines = []
while True:
    line = input("Enter a line (leave empty to stop): ")
    if line:
        lines.append(line)
    else:
        break

print("\nLines entered by the user:")
for line in lines:
    print(line)
