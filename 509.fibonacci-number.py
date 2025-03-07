#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        return self.recursion(n)
        # self.memoization(n)
    
    def recursion(self, n):
        if n<=1: return n
        return self.recursion(n-1)+self.recursion(n-2)
        
    def memoization(self, n):
        pass
        
# @lc code=end

