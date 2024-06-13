temp = input("Enter the temperature to convert (e.g., 32F, 100C): ")
degree = int(temp[:-1])
unit = temp[-1]

if unit.upper() == 'C':
    result = int(round((9 * degree) / 5 + 32))
    out_unit = 'Fahrenheit'
elif unit.upper() == 'F':
    result = int(round((degree - 32) * 5 / 9))
    out_unit = 'Celsius'
else:
    print("Invalid input. Please enter the temperature followed by 'C' or 'F'.")
    quit()

print(f"The temperature is {result} {out_unit}.")
