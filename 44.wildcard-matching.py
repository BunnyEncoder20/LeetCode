#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def recursive(i, j):
            # base case: both strings exhausted
            if i < 0 and j < 0:
                return True

            # base case: pattern exhausted
            if i >= 0 and j < 0: 
                return False

            # base case: primary exhasted 
            # (could convert pattern to empty string)
            if i < 0 and j >= 0:
                return all([ch == "*" for ch in p[:j+1]])
            
            # normally
            # matching char or '?' case
            if s[i] == p[j] or p[j] == '?':
                return recursive(i-1, j-1)
            
            # not matching but '*' case 
            if p[j] == "*":
                return recursive(i-1, j) or recursive(i, j-1)
            
            # not match and no "?" or "*"
            return False 
            
            
        n,m = len(s), len(p)
        return recursive(n-1, m-1)
        
# @lc code=end

