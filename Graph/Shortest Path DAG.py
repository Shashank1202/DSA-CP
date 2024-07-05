'''Problem Link
https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1
'''

from collections import deque
class Solution:
    def shortestPath(self, n, graph, src):
        dis=[float('inf') for _ in range(n)]

        adjList=[[] for _ in range(n)]
        for it in graph:
            adjList[it[0]].append(it[1])
            adjList[it[1]].append(it[0])

        q= deque()
        q.append(src)
        dis[src]=0

        while q:
            node=q.popleft()
            for neighbour in adjList[node]:
                if dis[node]+1 < dis[neighbour]:
                    dis[neighbour]= dis[node]+1
                    q.append(neighbour)

        ans= [-1]*n

        for i in range(n):
            if dis[i]!=float('inf'):
                ans[i]= dis[i]

        return ans


def main():
    n= 5
    graph=[[0, 1],[0, 2],[1, 3], [2, 4]]

    sol=Solution()
    ans=sol.shortestPath(n, graph, 0)
    print(ans)

if __name__=="__main__":
    main()

