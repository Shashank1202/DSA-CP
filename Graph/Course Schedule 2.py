'''Problem link
https://leetcode.com/problems/course-schedule-ii/submissions/1295305494/
'''

from collections import deque
class Solution:
    def course(self, v, prerequisites):
        adj= [[] for _ in range(v)]
        for it in prerequisites:
            adj[it[1]].append(it[0])

        in_degree=[0]*v
        for i in range(v):
            for node in adj[i]:
                in_degree[node]+=1

        q= deque()
        for i in range(v):
            if in_degree[i]==0:
                q.append(i)
        job=[]
        while q:
            node= q.popleft()
            job.append(node)

            for it in adj[node]:
                in_degree[it]-=1
                if in_degree[it]==0:
                    q.append(it)

        if len(job)==v:
            return job
        return []

n= 4
prerequisites= [[0, 1], [1, 2], [2, 3]]

sol= Solution()
ans= sol.course(n, prerequisites)
print("The ans ", ans)
