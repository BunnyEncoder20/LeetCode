#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # recursive helper func
        def backtracking(start, subset):
            # append the current subset
            res.append(subset[:])

            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtracking(i+1, subset)
                subset.pop()
            
        res = []
        backtracking(0, [])
        return res
        
# @lc code=end

