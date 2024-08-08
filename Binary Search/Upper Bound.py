def upperBound(arr, x):
    n= len(arr)
    for i in range(n):
        if arr[i]>x:
            return i
        
arr= [1, 3, 5, 6, 7, 8]
x= 6
res= upperBound(arr, x)
print(res)