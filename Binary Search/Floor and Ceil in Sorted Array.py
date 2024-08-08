def floorValue(arr, key):
    n=len(arr)
    low= 0
    high= n-1
    ans= -1
    while low<=high:
        mid= (low+high)//2
        if arr[mid]>=key:
            ans= arr[mid]
            high= mid-1
        else:
            low= mid+1
    return ans

def ceilValue(arr, key):
    n=len(arr)
    low= 0
    high= n-1
    ans= -1
    while low<=high:
        mid= (low+high)//2
        if arr[mid]<=key:
            ans= arr[mid]
            low= mid+1
        else:
            high= mid-1
    return ans


arr=[3, 4, 4, 7, 8, 10]
key= 5
print(ceilValue(arr, key))
print(floorValue(arr, key))