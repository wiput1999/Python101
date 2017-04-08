def isPrime(n):
    count = 0
    i = 1
    while i <= n:
        if n % i == 0:
            count+=1
        else:
            pass
        i+=1
    if count == 2: #isPrime = True
        return 0
    else:
        return 1

print(isPrime(17))