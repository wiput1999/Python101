def large(a,b):
    return a if a > b else b

def large3(a,b,c):
    m = a
    m = large(m,b)
    m = large(m,c)
    return m

print(large3(4,7,1))
