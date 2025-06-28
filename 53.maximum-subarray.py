#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxi = float('-inf')
        
        for num in nums:
            sum += num 
            if sum > maxi: maxi = sum 
            if sum < 0: sum = 0
        
        return maxi        
          
# @lc code=end

