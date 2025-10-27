def corrupt(s):
    corr = []
    for ch in s :
        n = ord(ch)
        corr.append(str(n * n + 1))
    return ",".join(corr)

def restore(s):
    corr = s.split(",")
    restored = ""
    for j in s :
        num = int(j)
        n = int((num - 1)**0.5)
        restored += chr(n)
    return restored


s = input("enter sentence : ")

corr = corrupt(s)

print(corr)
print(restore(corr))