from functools import reduce

numbers = [number for number in range(1, 51)]


def add(a, b):
    return a + b



result = reduce(add, numbers)

print(result) 
