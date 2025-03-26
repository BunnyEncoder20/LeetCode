#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
from functools import cache
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def lcs(i, j):
            # base case
            if i<0 or j<0: 
                return 0
            
            # matched
            if s[i] == t[j]:
                return 1 + lcs(i-1, j-1)
            
            # not matched
            else:
                return max(lcs(i-1, j), lcs(i, j-1))
            
        n = len(s)
        t = s[::-1]
        return lcs(n-1, n-1)
        # return self.lcs(s, s[::-1])
    
    def lcs(self, s, t):
        pass
        
        
# @lc code=end

