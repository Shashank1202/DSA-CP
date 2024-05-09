'''Problem Link:|
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
'''

class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        i = 0
        for j in range(1, len(arr)):
            if arr[i] != arr[j]:
                i += 1
                arr[i] = arr[j]
        return i + 1
