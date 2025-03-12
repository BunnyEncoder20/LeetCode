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
      start, ansStart, ansEnd = 0, 0, 0
      
      for i in range(len(nums)):
        sum += nums[i]
        if sum > maxsum:
          maxsum = sum
          ansStart = start
          ansEnd = i
          
        if sum < 0:
          sum = 0
          start = i+1
      
      return [ansStart, ansEnd]
            
          
# @lc code=end

