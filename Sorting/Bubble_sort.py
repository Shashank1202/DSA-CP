class Solution:
    def Bubble_sort(self, arr):
        n=len(arr)
        for i in range(n-1):
            count=0
            for j in range(n-i-1):
                if(arr[j]>arr[j+1]):
                    arr[j], arr[j+1]= arr[j+1],arr[j]
                    count=1
                if(count==1):
                    print("Run")
        return arr

sol=Solution()
arr=[1,2,3]
sorted_arr= sol.Bubble_sort(arr)
print(sorted_arr)
