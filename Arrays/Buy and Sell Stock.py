'''Brute Force 0(n^2)
def buySell(arr):
    n= len(arr)
    maxi =0
    for i in range(n-1):
        for j in range(1, n):
            maxi= max(maxi, arr[j]- arr[i])
    return maxi
'''

#Optimal Solution

def buySell(arr):
    n= len(arr)
    mini= float('inf')
    maxi= 0
    for i in range(n):
        mini= min(mini, arr[i])
        maxi= max(maxi, arr[i]- mini)
    return maxi


arr=[2, 1, 4, 3, 7]

print(arr)
print(buySell(arr))


