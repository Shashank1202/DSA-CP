''' Problem link:|
https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
'''
#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        meeting=[(start[i], end[i]) for i in range(n)]
        
        meeting.sort(key=lambda x:x[1])
        
        max_meeting=1
        cur_end=meeting[0][1]
        
        for i in range(1,n):
            if meeting[i][0]>cur_end:
                max_meeting+=1
                cur_end=meeting[i][1]
        return max_meeting
        
