'''Problem Link
https://www.geeksforgeeks.org/problems/topological-sort/1
'''

class Solution:
    def Topo(self,v, adj):
        vis=[0 for _ in range(v)]
        st=[]
        for node in range(v):
            if not vis[node]:
                self.dfs(node, vis, adj, st)
        ans=[]
        while st:
            ans.append(st.pop())
        return ans

    def dfs(self, node, vis, adj, st):
        vis[node]=1
        for neighbour in adj[node]:
            if not vis[neighbour]:
                self.dfs(neighbour, vis, adj, st)
        st.append(node)
def adjNode(adjList, u, v):
    adjList[u].append(v)

def main():
    v= 6
    adjList=[[] for _ in range(v)]

    adjNode(adjList, 5, 2)
    adjNode(adjList, 5, 0)
    adjNode(adjList, 4, 0)
    adjNode(adjList, 4, 1)
    adjNode(adjList, 2, 3)
    adjNode(adjList, 3, 1)

    sol= Solution()
    ans= sol.Topo(v, adjList)
    print("The Ans is ", ans)

if __name__=="__main__":
    main()
