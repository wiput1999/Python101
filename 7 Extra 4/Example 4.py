def ipow(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    if n % 2 == 1:
        return a * ipow(a, n-1)
    t = ipow(a, n//2)
    return t**2

print(ipow(2, 10))
