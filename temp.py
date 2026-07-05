def sum_all(*numbers):
    number = 0
    for i in numbers:
        number = number + i
    return number

print(sum_all(1,2,3))