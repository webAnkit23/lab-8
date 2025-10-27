def fact(n):
    fact  = 1
    for i in range(1, n + 1):
        fact *=i
    return fact

def combinations(n,r):
    if r > n:
        return 0
    return fact(n)//(fact(r)*fact(n-r))

n = int(input("enter n : "))
r = int(input("enter r : "))

print(combinations(n,r))
