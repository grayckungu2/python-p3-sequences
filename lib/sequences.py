def print_fibonacci(length):
    fibonacci = [0, 1]
    while len(fibonacci) < length:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    print(fibonacci)

print_fibonacci(9) 