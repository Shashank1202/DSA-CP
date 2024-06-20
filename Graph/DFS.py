class Solution:
    def dfsOfGraph(self, V, adj):
        visited = [0] * V
        values = []
        self.dfs(0, adj, visited, values)
        return values
    def dfs(self, node, adj, visited, values):
        visited[node] = 1
        values.append(node)
        for i in adj[node]:
            if visited[i] == 0:
                self.dfs(i, adj, visited, values)
def addEdge(adj, u, v):
    adj[u].append(v)
def printAns(ans):
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    V = 5
    adj = [[] for _ in range(V)]

    # Adding edges to the graph
    addEdge(adj, 0, 2)
    addEdge(adj, 2, 4)
    addEdge(adj, 0, 1)
    addEdge(adj, 0, 3)

    # Creating an instance of Solution class
    sol = Solution()
    # Calling the DFS traversal function
    result = sol.dfsOfGraph(V, adj)
    # Printing the result
    print("The DFS traversal of the graph is:")
    printAns(result)
