#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def recursive(i, need):
            # base case
            if need == 0:
                return True
            if i == 0:
                return nums[0] == need
            
            # dp check
            if dp[i][need] != -1:
                return dp[i][need]
            
            # normally
            # not pick
            notpick = recursive(i-1, need)
            
            # pick
            pick = False
            if nums[i] < need:
                pick = recursive(i-1, need - nums[i])
            
            dp[i][need] = pick or notpick
            return dp[i][need]

        n = len(nums)
        total = sum(nums)
        if total % 2 == 1: 
            return False
        else: 
            k = total//2
            dp = [[-1] * (k+1) for _ in range(n)]
            return recursive(n-1, total//2)
            
             
                 
            
       
       
# @lc code=end

