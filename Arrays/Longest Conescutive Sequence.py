'''def longSeq(arr):
    n= len(arr)
    longest=1
    for i in range(n):
        x= arr[i]
        cnt=1
        while linearSearch(arr, x+1):
            x+=1
            cnt+=1
        longest= max(longest, cnt)
    return longest

def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i]==x:
            return True
    return False
'''

'''def longSeq(arr):
    arr.sort()
    longest = 1
    cnt= 1

    for i in range(1, len(arr)):
        if arr[i]== arr[i-1]+1:
            cnt+=1
        elif arr[i]!= arr[i-1]:
            cnt=1
        longest= max(longest, cnt)
    return longest

'''

def longSeq(arr):
    st= set()
    longest=1
    for i in range(len(arr)):
        st.add(arr[i])

    for it in st:
        if it-1 not in st:
            cnt=1
            x= it

            while x+1 in st:
                x+=1
                cnt+=1
            longest= max(cnt, longest)
    return longest

    

arr=[1,7, 3, 2]
print(longSeq(arr)) 