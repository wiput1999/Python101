def powerof2(n):
    a = 1
    while a < n:
        a*=2
    return a

print(powerof2(16))