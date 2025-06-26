#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        mpp = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0

        for i in range(len(s)):
            if i+1<len(s) and mpp[s[i]] < mpp[s[i+1]]:
                result -= mpp[s[i]]
            else:
                result += mpp[s[i]]

        return result
        
# @lc code=end

