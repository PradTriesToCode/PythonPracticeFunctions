def calc(a, b):
    if a >= b:
        return (a + b, a - b)
    else:
        return (a - b, a + b)
a = int(input("\nEnter your first number: "))
b = int(input("Enter your second number: "))

print("\nYour numbers are: ", "(", a, b, ")")

result = calc(a, b)

print("\n", result)
