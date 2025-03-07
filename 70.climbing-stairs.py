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

    def tabulation(self, n):
        # base case
        if n <= 1: return 1
        
        # init 
        curr,prev2,prev1 = None,1,1
        
        for i in range(2,n+1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        
        return curr
        
        
        
    
        
# @lc code=end

