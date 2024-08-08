'''def lowerBound(arr, x):
    n= len(arr)
    for i in range(n):
        if arr[i]>=x:
            return i
   '''

def lowerBound(arr, x):
    n= len(arr)
    low= 0
    high= n-1
    while low<=high:
        mid= (low+high)//2
        if arr[mid]>=x:
            return mid
            high= mid-1
        else:
            low= mid+1
    return -1    

arr=[3, 5, 8, 15, 19]
x= 9
res= lowerBound(arr, x)
print(res)