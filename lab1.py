def fibonacci_iterative(n):
    a, b = 0, 1

    with open("output/fibonacci.txt", "w") as file:
        for _ in range(n):
            file.write(str(a) + "\n")
            a, b = b, a + b


fibonacci_iterative(25)
