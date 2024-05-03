Problem Link:  https://leetcode.com/problems/sort-colors/description/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        '''
        Better SOlution

        cnt0=0
        cnt1=0
        cnt2=0
        for i in nums:
            if i==0:
                cnt0+=1
            if i==1:
                cnt1+=1
            if i==2:
                cnt2+=2
        for i in range(cnt0):
            nums[i]=0
        for i in range(cnt0, cnt0+cnt1):
            nums[i]=1
        for i in range(cnt0+cnt1, len(nums)):
            nums[i]=2  
            
            Optimal Solution '''

        low=0
        mid=0
        high=len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[low],nums[mid]= nums[mid], nums[low]
                mid+=1
                low+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]= nums[high], nums[mid]
                high-=1
        
