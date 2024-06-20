class Solution:
    def dfs(self, node, adjList, vis):
        vis[node]=True
        for neighbour in adjList[node]:
            if not vis[neighbour]:
                self.dfs(neighbour, ajdList, vis)


    def province(self, adj, v):
        adjList= [[] for _ in range(v)]

        for i in range(v):
            for j in range(v):
                if adj[i][j]==1 and i!=j:
                    adjList[i].append(j)
                    adjList[j].append(i)

        vis= [False]*v
        cnt= 0

        for i in range(v):
            if not vis[i]:
                cnt+=1
                self.dfs(i, adjList, vis)
        return cnt

adj = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]

solution = Solution()
print(solution.province(adj, 3))
