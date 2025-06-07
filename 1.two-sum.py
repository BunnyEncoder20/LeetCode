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
        mpp = [(nums[i], i) for i in range(len(nums))]
        mpp.sort(key= lambda x: x[0])
        left, right = 0, len(nums)-1
        
        while left<right:
            if mpp[left][0] + mpp[right][0] == target:
                return [mpp[left][1], mpp[right][1]]
            elif mpp[left][0] + mpp[right][0] < target:
                left += 1
            else:
                right -= 1
        
        return [-1,-1]
            
# @lc code=end

