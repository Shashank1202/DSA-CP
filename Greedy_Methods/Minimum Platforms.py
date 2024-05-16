'''Problem Link:|
https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1
'''
#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        arr.sort()
        dep.sort()
        
        i=0
        j=0
        platform=0
        max_platform=0
        
        while i<n and j<n:
            if arr[i]<=dep[j]:
                platform+=1
                i+=1
            elif arr[i]>dep[j]:
                platform-=1
                j+=1
            max_platform=max(max_platform, platform)
        return max_platform
