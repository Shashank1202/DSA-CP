'''Problem Link:
https://leetcode.com/problems/rotting-oranges/
'''

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #Base cases
        row=len(grid)
        if row==0:
            return -1
        
        col=len(grid[0])
        fresh_cnt=0
        rotten= deque()

        for r in range(row):
            for c in range(col):
                if grid[r][c]==2:
                    rotten.append((r, c))
                elif grid[r][c]==1:
                    fresh_cnt+=1

        minute_passed=0

        while rotten and fresh_cnt>0:
           minute_passed+=1

        
            for _ in range(len(rotten)):
                 x, y= rotten.leftpop()
            
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xx, yy= x+dx, y+dy

                    if xx<0 or xx=row or yy<0 or yy=row:
                        continue
                    
                    if grid[xx][yy]

