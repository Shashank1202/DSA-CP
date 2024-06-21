'''Problem Link
https://www.geeksforgeeks.org/problems/topological-sort/1
'''

from collections import deque

class Solution:
    def Topo(self, v, adj):
        in_degree=[0]*v

        for i in range(v):
            for neighbour in adj[i]:
                in_degree[neighbour]+=1

        q= deque(i for i in range(v) if in_degree[i]==0)

        topo_order= []
        while q:
            node= q.popleft()
            topo_order.append(node)
            for neighbour in adj[node]:
                in_degree[neighbour]-=1
                if in_degree[neighbour]==0:
                    q.append(neighbour)

        if len(topo_order)==v:
            return topo_order
        else:
            return []

def adjNode(adjlist, u, v):
    adjlist[u].append(v)
def main():
    v= 4
    adjlist=[[] for _ in range (v)]

    adjNode(adjlist,0, 1)
    adjNode(adjlist, 0, 2)
    adjNode(adjlist, 0, 3)
    adjNode(adjlist, 1, 3)
    adjNode(adjlist, 2, 3)

    sol= Solution()

    ans= sol.Topo(v, adjlist)
    print("The ans: ",ans)

if __name__=="__main__":
    main()
