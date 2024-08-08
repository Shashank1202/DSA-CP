'''def searchPosition(arr, key):
    n= len(arr)
    for i in range(n-1):
        if arr[i]< key and key<=arr[i+1]:
            return i+1
    
    if key >arr[-1]:
        return n
    
    return -1
'''

def searchPosition(arr, key):
    n= len(arr)
    low=0
    high= n-1
    ans=n
    while low<=high:
        mid= (low+high)//2
        if arr[mid]>=key:
            ans= mid
            high= mid-1
        else:
            low= mid+1
    return ans
        
arr =[1, 2, 4, 6, 7]
key= 5
res= searchPosition(arr, key)
print(res)