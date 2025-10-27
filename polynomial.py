def polynomials_op(p1, p2,op):
   
    max_len = max(len(p1), len(p2))
    p1 += [0] * (max_len - len(p1))
    p2 += [0] * (max_len - len(p2))
    
   
    return [p1[i] + p2[i] if op == 1 else p1[i] - p2[i] for i in range(max_len)]


P = [1, 2, 3]     
Q = [4, 0, 5, 6]   
n = int(input("press 1 for addition an 2 for subtraction : "))
if n != 1 and n != 2:
    print("invalid choice")

else:
    result = polynomials_op(P, Q, n)
    print(result)  

   

