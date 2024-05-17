'''Problem Link:|
https://leetcode.com/problems/subsets-ii/description/
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output, stack= [], []

        def fn(i):
            if i>=len(nums):
                output.append(stack.copy())
                return
        
            stack.append(nums[i])
            fn(i+1)

            stack.pop()
            while i+1 < len(nums) and nums[i]==nums[i+1]:
                i+=1

            fn(i+1)
        
        fn(0)
        return output
