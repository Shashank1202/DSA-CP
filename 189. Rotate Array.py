'''189. Rotate Array

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100] '''


class Solution(object):
    def rotate(self, nums, k):
       n=len(nums)
       k=k%n
       self.reverse(nums, n-k,n-1)
       self.reverse(nums, 0,n-k-1)
       self.reverse(nums,0, n-1)

    def reverse(self, nums, start, end):
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1
