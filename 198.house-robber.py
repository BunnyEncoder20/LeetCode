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

            # normally
            # not rob
            notrob = 0 + recursive(i-1)

            # rob
            rob = nums[i] + recursive(i-2)

            # return the best
            return max(rob, notrob)
        
        n = len(nums)
        return recursive(n-1)
        
        
# @lc code=end

