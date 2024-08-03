'''def setMatrixZero(matrix):
    n= len(matrix)
    m= len(matrix[0])

    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                markRow(matrix, n, m, i)
                markCol(matrix, n, m, j)
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==-1:
                matrix[i][j]=0
    return matrix

def markRow(matrix, n, m, row):
    for j in range(m):
        matrix[row][j]=-1
    
def markCol(matrix, n, m, col):
    for i in range(n):
        matrix[i][col]=-1

'''

'''def setMatrixZero(matrix):
    n= len(matrix)
    m= len(matrix[0])

    row= [0]*n
    col= [0]*m
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                row[i]=1
                col[i]=1
    
    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                matrix[i][j]=0

    return matrix
'''

def setMatrixZero(matrix):
    n= len(matrix)
    m= len(matrix[0])
    col0=1

    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                matrix[i][0]=0
                if j!=0:
                    matrix[0][j]=0
            else:
                col1=0
    
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j]!=0:
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0


            if matrix[0][0]==0:
                for j in range(m):
                    matrix[0][j]=0
            if col0==0:
                for i in range(n):
                    matrix[i][0]=0

    return matrix
    

matrix=[
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

print(setMatrixZero(matrix))


'''[1, 1, 1]
[1, 0, 1]   
[1, 1, 1]

[1, -1, 1]
[-1, 0,-1]
[1, -1, 1]

[1, 0, 1]
[0, 0, 0]
[1, 0, 1]

0(nxm) + 0(n) + 0(m) + 0(nxm)

0(1)

[1, 1, 1]
[1, 0, 1]   
[1, 1, 1]

[0, 1, 0]= Row 

[0,1, 0]= col

[1,0,1]
[0, 0, 0]
[1,0, 1]

0(nXm) + 0(nXm)

0(n), 0(m)



'''