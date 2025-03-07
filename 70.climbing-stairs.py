#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # return self.recursion(n)
        # return self.memoization(n)
        return self.tabulation(n)

    def recursion(self, n):
        if n <= 1: return 1
        return self.recursion(n-1) + self.recursion(n-2)
    
    def memoization(self, n):
        def recursive(n):
            if n <= 1: return 1
            if dp[n] != -1: return dp[n]
            dp[n] = recursive(n-1) + recursive(n-2)
            return dp[n]
        
        # base case 
        if n <= 1: return 1
        
        # init
        dp = [-1] * (n+1)
        dp[0],dp[1] = 1,1
        recursive(n)
        return dp[n]
    
        
# @lc code=end

