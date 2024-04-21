26. Remove Duplicates from Sorted Array
##https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution(object):
    def removeDuplicates(self, nums):
        '''Brute for approach
        st=set()
        for i in range(len(nums)):
            st.add(nums[i])
        k=len(st)
        j=0
        for x in st:
            nums[j]=x
            j+=1
        return k'''
       
        '''optimal approach
        i=0
        for j in range(len(nums)):
            if nums[i]!=nums[j]:
                nums[i+1]=nums[j]
                i+=1
        return i+1'''
        