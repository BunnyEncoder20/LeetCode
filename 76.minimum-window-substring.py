#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        if m > n: return ""
        
        l,r,count = 0,0,m
        minlen, startIdx = n,None
        fpp = Counter(t)
        
        while r < n:
            # the char was in t string
            if s[r] in fpp:
                if fpp[s[r]] > 0: count -= 1
                fpp[s[r]] -= 1
            
            # covered all t chars
            while count == 0:
                if minlen >= r-l+1:
                    minlen = r-l+1
                    startIdx = l
                
                if s[l] in fpp:
                    fpp[s[l]] += 1
                    if fpp[s[l]] > 0:
                        count += 1
                l += 1
            r += 1    
        
        # print(startIdx)
        # print(s[startIdx:startIdx+minlen])
        if startIdx != None:
            return s[startIdx:startIdx+minlen] 
        else:
            return ""
        
# @lc code=end

