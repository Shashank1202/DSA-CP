'''Problem Link:

https://leetcode.com/problems/merge-intervals/description/
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        intervals.sort()
        ans=[]
        for i in range(n):
            if not ans or intervals[i][0]>ans[-1][1]:
                ans.append(intervals[i])
            else:
                ans[-1][1]=max(ans[-1][1], intervals[i][1])
        return ans

        
