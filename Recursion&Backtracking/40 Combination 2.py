'''
Problem Link:
https://leetcode.com/problems/combination-sum-ii/submissions/1263094546/
'''


from typing import List
class Solution:
    def Combination2(self, candidates: List[int],target: int )-> List[List[int]]:
        ans=[]
        ds=[]
        candidates.sort()

        def Combi(ind: int, target: int):
            if target==0:
                ans.append(ds[:])
                return

            for i in range(ind, len(candidates)):
                if i> ind and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                ds.append(candidates[i])
                Combi(i + 1, target- candidates[i])
                ds.pop()
        Combi(0, target)
        return ans

if __name__=='__main__':
    candidates=[10, 1, 2, 7, 6, 1, 5]
    obj=Solution()
    comb=obj.Combination2(candidates, 8)
    print(*comb)

