'''Problem Link
https://leetcode.com/problems/surrounded-regions/
'''


class Solution:
    def dfs(self, row, col, vis, mat, delrow, delcol):
        vis[row][col]= True
        n= len(mat)
        m= len(mat[0])

        for i in range(4):
            nrow = row + delrow[i]
            ncol = col + delcol[i]
            # check for valid coordinates and unvisited 'O's
            if 0 <= nrow < n and 0 <= ncol < m and not vis[nrow][ncol] and mat[nrow][ncol] == 'O':
                self.dfs(nrow, ncol, vis, mat, delrow, delcol)
    
    def solve(self, mat: List[List[str]]) -> None:
        n= len(mat)
        m= len(mat[0])
        delrow = [-1, 0, 1, 0]
        delcol = [0, 1, 0, -1]
        vis = [[False for _ in range(m)] for _ in range(n)]
        
        # traverse first row and last row
        for j in range(m):
            # check for unvisited 'O's in the boundary rows
            # first row
            if not vis[0][j] and mat[0][j] == 'O':
                self.dfs(0, j, vis, mat, delrow, delcol)
            
            # last row
            if not vis[n-1][j] and mat[n-1][j] == 'O':
                self.dfs(n-1, j, vis, mat, delrow, delcol)
        
        for i in range(n):
            # check for unvisited 'O's in the boundary columns
            # first column
            if not vis[i][0] and mat[i][0] == 'O':
                self.dfs(i, 0, vis, mat, delrow, delcol)
            
            # last column
            if not vis[i][m-1] and mat[i][m-1] == 'O':
                self.dfs(i, m-1, vis, mat, delrow, delcol)
        
        # if unvisited 'O' then convert to 'X'
        for i in range(n):
            for j in range(m):
                if not vis[i][j] and mat[i][j] == 'O':
                    mat[i][j] = 'X'
        
        return mat
        
