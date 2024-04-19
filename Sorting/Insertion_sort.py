class Solution:
    def Insertion_sort(self,  arr):
        n= len(arr)
        for i in range(n):
            j=i
            while j>0 and arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
                j-=1
        return arr

sol=Solution()
arr=[19,2,1,4]
sorted_arr=sol.Insertion_sort(arr)
print(arr)