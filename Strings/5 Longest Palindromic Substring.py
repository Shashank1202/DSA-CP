'''Problem link:
https://leetcode.com/problems/longest-palindromic-substring/
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        n = len(s)
        max_len = 1
        st, en = 0, 0

        def expandAroundCenter(left: int, right: int) -> (int, int):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1
        
        for i in range(n):
            # Odd length palindromes
            l, r = expandAroundCenter(i, i)
            if r - l + 1 > max_len:
                max_len = r - l + 1
                st, en = l, r
            
            # Even length palindromes
            l, r = expandAroundCenter(i, i + 1)
            if r - l + 1 > max_len:
                max_len = r - l + 1
                st, en = l, r
        
        return s[st:en + 1]
