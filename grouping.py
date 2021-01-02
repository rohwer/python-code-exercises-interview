"""
Given a list of values inputs and a positive integer n, write a function that splits inputs into groups of length n. For simplicity, assume that the length of the input list is divisible by n. For example, if inputs = [1, 2, 3, 4, 5, 6] and n = 2, your function should return [(1, 2), (3, 4), (5, 6)].

[1] https://realpython.com/python-itertools/
[2] https://docs.python.org/3.6/library/itertools.html#itertools-recipes
"""
from itertools import zip_longest
def grouper(iterable, n, fillvalue=None):
    "collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

if __name__ == "__main__":
    ls = [i for i in range(1,7)]
    n = 2
    print(list(grouper(ls,2)))
