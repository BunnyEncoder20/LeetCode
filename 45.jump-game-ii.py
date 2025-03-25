#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
from functools import cache
class Solution:
    def jump(self, nums: List[int]) -> int:
        # init
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0   # no steps needed to get to first idx
        
        for i in range(n):
            for jumps in range(1, nums[i]+1):
                if i+jumps < n:
                    dp[i+jumps] = min( dp[i+jumps], dp[i]+1)
        
        return dp[n-1]
        
# @lc code=end

