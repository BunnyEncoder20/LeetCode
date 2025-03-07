#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        # return self.recursion(n)
        # return self.memoization(n)
        # return self.tabulation(n)
        return self.spaceOptimizedTabulation(n)
    
    def recursion(self, n):
        if n<=1: return n
        return self.recursion(n-1)+self.recursion(n-2)
        
    def memoization(self, n):
        def recursive(n):
            if n<=1: return n
            if dp[n] != None: return dp[n]
            dp[n] = recursive(n-1) + recursive(n-2)
            return dp[n]

        # init
        dp = [None] * (n+1)
        res = recursive(n)
        return res
    
    def tabulation(self, n):
        # base case 
        if n == 0: return 0
        if n == 1: return 1
        
        # init
        dp = [None] * (n+1)
        dp[0],dp[1] = 0,1
        
        # remaining cases: use recursive relation
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
        
    
    def spaceOptimizedTabulation(self, n):
        # base case 
        if n == 0: return 0
        if n == 1: return 1 
        
        # init 
        prev2 = 0
        prev1 = 1
        curr = None
        
        # remaining cases
        for i in range(2,n+1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
            
        return curr
        
        
# @lc code=end

