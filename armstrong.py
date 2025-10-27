def armstrong(n):
    len = len(str(n))
    sum = 0
    temp = n

    while temp > 0:
        dig =  temp % 10
        sum += dig**len
        temp = temp//2
    return sum == n

num = int(input("enter a number : "))
print(armstrong(num))