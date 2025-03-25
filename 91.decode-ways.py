#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def recursive(i):
            # base case: reached end of string
            if i == n:
                return 1
            
            # base case: the current is zero
            if s[i] == "0":
                return 0
            
            # noramlly 
            onedigit, twodigits = 0,0
            
            # taking 1 digit
            onedigit = recursive(i+1)
            
            # taking 2 digits 
            if i+1 < len(s) and (
                s[i] == "1" or 
                s[i] == "2" and s[i+1] in "0123456"
            ): 
                twodigits = recursive(i+2)
            
            
            return onedigit + twodigits
            
        
        # trivial case
        if s[0] == "0": return 0

        n = len(s)
        return recursive(0)

        
# @lc code=end

