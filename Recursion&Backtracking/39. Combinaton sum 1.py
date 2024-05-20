'''https://leetcode.com/problems/combination-sum/description/
from typing import List
'''
class Solution:
    def Combination(self, candidates: List[int], target: int)-> List[List[int]]:
        ans= []
        ds= []

        def Combi(ind: int, target: int):
            if ind==len(candidates):
                if target==0:
                    ans.append(ds[:])
                return

            if candidates[ind]<=target:
                ds.append(candidates[ind])
                Combi(ind, target - candidates[ind])
                ds.pop()
            Combi(ind+1,target)

        Combi(0, target )
        return ans


if __name__=='__main__':
    obj=Solution()
    candidates=[2, 3, 6, 7]
    target=7
    ans=obj.Combination(candidates, target)
    print("Combination are ")
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end=" ")
        print()
