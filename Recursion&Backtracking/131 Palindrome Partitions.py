'''
Problem Link:
https://leetcode.com/problems/palindrome-partitioning/submissions/1263151602/
'''

from typing import List

class Solution:
    def Palindrome(self, s: str)->List[List[str]]:
        ans=[]
        path=[]

        def PalindromeHelper(ind: int):
            if ind==len(s):
                ans.append(path[:])
                return
            for i in range (ind, len(s)):
                if isPalindrome(s, ind, i):
                    path.append(s[ind:i+1])
                    PalindromeHelper(i+1)
                    path.pop()

        def isPalindrome(s: str, start: int, end: int)->bool:
            while start<=end:
                if s[start]!=s[end]:
                    return False
                start+=1
                end-=1
            return True

        PalindromeHelper(0)
        return ans


if __name__== '__main__':
    s="aabb"
    obj=Solution()
    ans=obj.Palindrome(s)
    print("The palindrome partitions are")
    print("[", end="")
    for i in ans:
        print("[ ", end="")
        for j in i:
            print(j, end="")
        print("] ", end="")
    print("]")





