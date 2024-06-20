'''Problem Link
https://leetcode.com/problems/01-matrix/submissions/1290790270/
'''

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []
        
        m,n= len(mat), len(mat[0])
        queue= deque()
        max_value=m*n

        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    queue.append((i, j))
                else:
                    mat[i][j]=max_value

        directions= [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            row, col= queue.popleft()
            for dr, dc in directions:
                r, c= row+dr, col+dc
                if 0<= r < m and 0<= c < n and mat[r][c] > mat[row][col]+1:
                    queue.append((r, c))
                    mat[r][c]=mat[row][col]+1
        return mat
