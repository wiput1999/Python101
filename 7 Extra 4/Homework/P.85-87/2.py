""" Docstring """
import sys

sys.setrecursionlimit(999999999)

def fac(n):
    """ Function Docstring """
    if n == 1 or n == 0:
        return 1
    return n * fac(n-1)

def res_sum(n):
    """ Function Docstring """

    num = str(n)
    result = 0
    for i in num:
        result += int(i)

    return result

RES = fac(10000)
print(res_sum(RES))
