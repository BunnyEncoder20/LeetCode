#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        # return self.recursion(n)
        return self.memoization(n)
    
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
        
# @lc code=end

