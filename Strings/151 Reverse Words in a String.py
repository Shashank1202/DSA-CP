'''Problem link
https://leetcode.com/problems/reverse-words-in-a-string/
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        result, i, n = '', 0, len(s)

        while i < n:
            while i < n and s[i] == ' ': i += 1
            if i >= n: break
            j = i + 1
            while j < n and s[j] != ' ': j += 1
            sub = s[i:j]
            if len(result) == 0:
                result = sub
            else:
                result = sub + " " + result
            i = j + 1
        return result

if __name__=="__main__":
    sol=Solution()
    s= " Hello  World!  "
    res=sol.reverseWords(s)
    print(res)
