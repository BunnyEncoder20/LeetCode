#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # init 
        n,m = len(s),len(p)
        dp = [[False] * (m+1) for _ in range(n+1)]
        
        # base case: both strings exhausted 
        dp[0][0] = True
        
        # base case: pattern exhausted (j=0)
        for i in range(1, n+1):
            dp[i][0] = False
        
        # base case: primary exhausted (i=0)
        for j in range(1, m+1):
            if p[j-1] == "*":
                # '*' can act as empty string seq
                dp[0][j] = dp[0][j-1]
            else:
                # once non '*' char encountered, it cannot behave 
                # as empty string
                break
        
        # Fill dp table
        for i in range(1, n+1):
            for j in range(1, m+1):
                # matching char or '?' case 
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                
                # not matching but '*' case
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                
                # not matching and no '?' or '*' 
                else:
                    dp[i][j] = False
        
        # return ans
        return dp[n][m]
        
# @lc code=end

