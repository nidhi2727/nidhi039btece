n = int(input("Enter the number of Fibonacci numbers to generate: "))
a, b = 0, 1
print("First", n, "Fibonacci numbers:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
