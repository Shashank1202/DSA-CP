def binarySearch(arr,low, high, key):
    n= len(arr)
    while low<= high:
        mid= (low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low= mid+1
        else:
            high= mid-1
    return -1


arr= [1, 2, 4, 5, 6, 9]
key= 6
n= len(arr)
res= binarySearch(arr, 0, n-1, key)
print("Element found at",res+1)