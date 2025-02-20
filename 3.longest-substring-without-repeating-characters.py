#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        mpp = {}
        l,r = 0,0
        maxlen = float('-inf')

        while r < len(s):
            if s[r] in mpp and l <= mpp[s[r]]:
                l = mpp[s[r]]+1
                
            mpp[s[r]] = r
            maxlen = max(maxlen, r-l+1)
            r += 1
        
        return maxlen
        
# @lc code=end

