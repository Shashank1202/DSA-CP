class Solution:
    def isCycle(self, v, adjList)->bool:
        vis= [0]*v
        for i in range(v):
            if not vis[i]:
                if self.dfs(i, -1, vis, adjList):
                    return True
        return False

    def dfs(self, node, parent, vis, adjList)->bool:
        vis[node]=1
        for neighbour in adjList[node]:
            if not vis[neighbour]:
                if self.dfs(neighbour, node, vis, adjList):
                    return True
                elif neighbour!= parent:
                    return True
        return False

def addAdj(adjList, u, v):
    adjList[u].append(v)
    adjList[v].append(u)

def main():
    vertices= 5
    adjList = [[] for _ in range(vertices)]

    addAdj(adjList,1, 2)
    addAdj(adjList,2, 3)
    addAdj(adjList,3, 4)
    addAdj(adjList,3, 1)

    sol= Solution()
    ans= sol.isCycle(vertices, adjList)
    if ans:
        print("True")
    else:
        print("False")

if __name__=="__main__":
    main()
