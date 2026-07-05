def multiply_args(*numbers):
    total = 1
    for n in numbers:
        total = total * n

    return total

print(multiply_args(1,2))