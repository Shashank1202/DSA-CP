'''def threeSum(arr):
    n= len(arr)
    st= set()
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if arr[i]+ arr[j]+ arr[k]==0:
                    temp= [arr[i], arr[j], arr[k]]
                    temp.sort()
                    st.add(tuple(temp))
    ans= [list(item) for item in st]

    return ans
'''

def threeSum(arr):
    n= len(arr)
    st= set()

    for i in range(n):
        hashset= set()
        for j in range(i+1,n):
            target= -(arr[i]+ arr[j])
            if target in hashset:
                temp= [arr[i], arr[j], target]
                temp.sort()
                st.add(tuple(temp))
            hashset.add(arr[j])
    
    ans= list(st)
    return ans

arr= [-1, 0, 1, 2, -1, -4]

print(threeSum(arr))