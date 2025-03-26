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
        dp = [[0] * (n+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(
                        dp[i-1][j],
                        dp[i][j-1]
                    )

        return dp[n][n]
        
        
        
# @lc code=end

