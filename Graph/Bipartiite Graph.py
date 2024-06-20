'''
Problem Link
https://leetcode.com/problems/is-graph-bipartite/description/
'''

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n= len(graph)
        color= [-1]*n
        for i in range(n):
            if color[i]==-1:
                if not self.dfs(i, 0, color, graph):
                    return False
        return True
    
    def dfs(self, node, col, color, graph)->bool:
        color[node]=col
        for i in graph[node]:
            if color[i]==-1:
                if not self.dfs(i, 1- col, color, graph):
                    return False
            elif color[i]==col:
                return False
        return True


        
