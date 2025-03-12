#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      maxsum = float('-inf')
      sum = 0
      
      for num in nums:
        sum += num
        if sum > maxsum:
          maxsum = sum
        if sum < 0:
          sum = 0
      
      return maxsum
            
          
# @lc code=end

