def convert(n) : 
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return convert(n//2) + str(n%2)

num = int(input("enter a deccimal no : "))
print(convert(num))

       