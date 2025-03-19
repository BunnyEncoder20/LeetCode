#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        def recursive(i):
            # base case
            if i == 0: return nums[0]
            if i < 0: return 0
            
            # dp check
            if dp[i] != -1: return dp[i]
            
            # normally
            # not rob
            notrob = 0 + recursive(i-1)

            # rob
            rob = nums[i] + recursive(i-2)

            # return the best
            dp[i] = max(rob, notrob)
            return dp[i]
        
        n = len(nums)
        dp = [-1] * n
        return recursive(n-1)
        
        
# @lc code=end

