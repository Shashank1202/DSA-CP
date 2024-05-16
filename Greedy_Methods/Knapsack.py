'''Problem LInk:
https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1
'''


class job:
    def __init__(self, id, deadline, profit):
        self.id=id
        self.deadline=deadline
        self.profit=profit


class Solution:
    def jobs(self, jobs):
        jobs.sort(key=lambda x:x.profit, reverse=True)
        maxi=jobs[0].deadline
        for i in range(1, len(jobs)):
            maxi=max(maxi, jobs[i].deadline)

        slot=[-1]*(maxi+1)
        jobsDone=0
        profit=0

        for i in range(len(jobs)):
            for j in range(jobs[i].deadline, 0, -1):
                if slot[j]==-1:
                    slot[j]=i
                    jobsDone+=1
                    profit+=jobs[i].profit
                    break
        return jobsDone, profit


if __name__=="__main__":
    jobs=[job(1, 4, 20), job(2, 1, 10), job(3, 1, 40), job(4, 1, 30)]
    count, profit= Solution().jobs(jobs)
    print(count, profit)
