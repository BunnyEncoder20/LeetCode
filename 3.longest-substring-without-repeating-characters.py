#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxlen = 0
        if n == 0: return maxlen
        mpp = {}

        l,r = 0,0
        while r < n:
            if s[r] in mpp:
                l = max(mpp[s[r]]+1, l)
                
            mpp[s[r]] = r
            maxlen = max(maxlen, r-l+1)
            
            r += 1
        
        return maxlen
        
# @lc code=end

