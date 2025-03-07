#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        return self.recursion(n)

    def recursion(self, n):
        if n <= 1: return 1
        return self.recursion(n-1) + self.recursion(n-2)
    
        
# @lc code=end

