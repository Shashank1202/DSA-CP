
'''problem link:|
https://www.geeksforgeeks.org/problems/subset-sums2234/1
'''

class Solution:
    def subset(self, arr: list[int], n: int)->list[int]:
        ans=[]

        def subsethelp( ind:int, sum:int):
            if ind==n:
                ans.append(sum)
                return
            subsethelp(ind+1, sum+arr[ind])

            subsethelp(ind+1, sum)
        subsethelp(0, 0)
        ans.sort()
        return ans


if __name__=="__main__":
    arr=[3, 2, 1]
    n=len(arr)
    ans=Solution().subset(arr, n)
    for sum in ans:
        print(sum, end=" ")
    print()

