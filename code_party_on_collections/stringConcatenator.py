from functools import reduce


words = ['I', 'love', 'Python']


def add_strings(item_a, item_b):

    return item_a + " " + item_b  



result = reduce(add_strings, words)


print(result)
