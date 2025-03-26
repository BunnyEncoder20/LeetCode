#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.lcs(s, s[::-1])
    
    def lcs(self, s, t):
        n = len(s)
        curr = [0] * (n+1)
        prev = [0] * (n+1)

        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(
                        prev[j],
                        curr[j-1]
                    )
            prev[:] = curr

        return prev[n]
        
        
        
# @lc code=end

