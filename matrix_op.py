def matix_op(A,B,op):
    rows = len(A)
    cols = len(A[0])

    if op in ["add","sub"] and (len(B) != rows or len(B[0]) != cols) : 
        return "invalid Matrix"
    if op == "mul" and len(A[0]) != len(B):
        return "invalid Matrix"
    
    res = []

    if op == 'add' or op == 'sub' :
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(A[i][j]  + B[i][j] if op == 'add' else A[i][j] - B[i][j])
            res.append(row)

    elif op == 'mul':
        for i in range(rows):
            row = []
            for j in range(len(B[0])):
                sum = 0
                for k in range (len(B)):
                    sum += A[i][k] * B[k][j]
                row.append(sum)
            res.append(row)
    
    else :
        return "invalid operation"
    
    return res

                                 