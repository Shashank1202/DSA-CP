class Solution:
    def BellMan(self, v, adj, s):
        dis=[float('inf')]*v
        dis[s]=0
        for i in range(v-1):
            for it in adj:
                u, v, wt= it
                if dis[u]!= float('inf') and dis[u] + wt < dis[v]:
                    dis[v]= dis[u] + wt

        #Checking for negative cycle
        for it in adj:
            u, v, wt = it
            if dis[u] != float('inf') and dis[u] + wt < dis[v]:
                return [-1]

        return dis

if __name__=='__main__':
    v= 6
    s= 0
    edges=[
        [3, 2, 6],
        [5, 3, 1],
        [0, 1, 5],
        [1, 5, -3],
        [1, 2, -2],
        [3, 4, -2],
        [2, 4, 3]
    ]

    sol= Solution()
    res= sol.BellMan(v, edges, s)
    print(res)
