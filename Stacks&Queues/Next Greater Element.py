'''Problem Link:
https://leetcode.com/problems/next-greater-element-i/
'''




from typing import List

class Solution:
    def nextGreateElement(self, nums:List[int])->List[int]:
        nge=[-1]*len(nums)
        stack=[]

        for i in range(2*len(nums)-1, -1, -1):
            while stack and stack[-1] <= nums[i%len(nums)]:
                stack.pop()

            if i<len(nums):
                if stack:
                    nge[i % len(nums)] = stack[-1]
            stack.append(nums[i % len(nums)])
        return nge


if __name__ == "__main__":
    obj=Solution()
    v = [2, 4, 6, 2, 9]
    res = obj.nextGreateElement(v)
    print("The next greater element is ")
    print(*res)


