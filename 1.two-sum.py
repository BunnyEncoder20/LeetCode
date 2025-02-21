#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mpp = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in mpp:
                return [mpp[need], i]
            mpp[nums[i]] = i
        return [-1,-1]
        
        
        
# @lc code=end

