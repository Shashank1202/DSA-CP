import heapq

class Solution:
    def dijkstra(self, v, adj, s):
        pq= []
        dis=[float('inf')]*v
        dis[s]=0
        heapq.heappush(pq, (0, s))

        while pq:
            dist, node= heapq.heappop(pq)

            for adjNode, adjW in adj[node]:
                if dist + adjW < dis[adjNode]:
                    dis[adjNode]= dist+ adjW
                    heapq.heappush(pq, (dis[adjNode], adjNode))

        return dis

if __name__=="__main__":
    v= 3
    e= 3
    s= 2

    adj=[[] for _ in range(v)]
    adj[0].append((1, 1))
    adj[0].append((2, 6))
    adj[1].append((0, 1))
    adj[1].append((2, 3))
    adj[2].append((0, 6))
    adj[2].append((1, 3))

    obj= Solution()
    res= obj.dijkstra(v, adj, s)
    for i in range(v):
        print(f" Shortest distance from node {s} to node {i} is {res[i]}")
