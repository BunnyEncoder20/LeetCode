#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0: return True
        
        clean = "".join([ch.lower() for ch in s if ch.isalnum()])
        n = len(clean)
        i,j = 0, n-1
        
        while i < j:
            if clean[i] != clean[j]: return False
            i += 1
            j -= 1
        
        return True

# @lc code=end

