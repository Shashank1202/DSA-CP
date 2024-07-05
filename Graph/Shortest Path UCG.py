'''Problem Link
https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1
'''

from collections import defaultdict, deque
class Solution:
    def dfs(self, node, adj, vis, st):
        vis[node]=1
        for neighbour, _ in adj[node]:
            if not vis[neighbour]:
                self.dfs(neighbour, adj, vis, st)
        st.append(node)

    def shortPath(self, n, m, edges):
        adj= defaultdict(list)

        for edge in edges:
            u, v, wt = edge
            adj[u].append((v, wt))

        vis=[0]*n
        st=[]
        for i in range(n):
            if not vis[i]:
                self.dfs(i, adj, vis, st)

        dis=[float('inf')]*n
        dis[0]=0
        while st:
            node= st.pop()
            if dis[node]!=float('inf'):
                for neighbour, wt in adj[node]:
                    if dis[node]+wt< dis[neighbour]:
                        dis[neighbour]=wt+ dis[node]
        ans=[]
        ans= [-1 if d==float('inf') else d for d in dis]
        return ans

if __name__ == "__main__":
    N, M = 6, 7
    edges = [[0, 1, 2], [0, 4, 1], [4, 5, 4], [4, 2, 2], [1, 2, 3], [2, 3, 6], [5, 3, 1]]
    obj = Solution()
    ans = obj.shortPath(N, M, edges)

    print(ans)
