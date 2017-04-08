def ipow(a,n):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result*=a
            n-=1
        n//=2
        a**=2
    return result

print(ipow(2,100))
