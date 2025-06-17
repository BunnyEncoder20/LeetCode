#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ele_idx_mpp = sorted(
            [[nums[i], i] for i in range(len(nums))],
            key=lambda x: x[0]
        )

        left, right = 0, len(nums)-1

        while left<=right:
            twosum = ele_idx_mpp[left][0] + ele_idx_mpp[right][0]

            if twosum == target:
                return [ele_idx_mpp[left][1], ele_idx_mpp[right][1]]
            elif twosum < target:
                left += 1
            else:
                right -= 1

        
        return [-1,-1]
            
# @lc code=end

