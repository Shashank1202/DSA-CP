def nge(arr):
    n= len(arr)

    index= -1

    for i in range(n-2, -1, -1):
        if arr[i]<arr[i+1]:
            index=i
            break
    
    if index==-1:
        arr.reverse()
        return arr
    
    for i in range(n-1, index, -1):
        if arr[i]>arr[index]:
            arr[i], arr[index]= arr[index], arr[i]
            break
    
    arr[index+1:]= reversed(a[index+1:])

    return arr


a= [2, 1, 5, 4, 3, 0, 0]
ans= nge(a)
for i in ans:
    print(i, end= " ")
