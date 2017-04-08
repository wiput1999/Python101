def isPrime(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return 1
        i+=1
    return 0

print(isPrime(11))