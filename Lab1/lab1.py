def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


with open("output/fibonacci.txt", "w") as file:
    for i in range(25):
        file.write(str(fibonacci_recursive(i)) + "\n")

# Adding Comment to Python file
