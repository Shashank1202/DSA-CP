'''def rotateMatrix(matrix):
    n= len(matrix)
    reversed=[[0 for _ in range(n)]for _ in range(n)]

    for i in range(n):
        for j in range(n):
            reversed[j][n-i-1]= matrix[i][j]
    return reversed

'''

def rotateMatrix(matrix):
    n= len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i]= matrix[j][i], matrix[i][j]
    

    for i in range(n):
        matrix[i].reverse()

    return matrix

matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]




print(matrix)
print(rotateMatrix(matrix))
