#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
from functools import cache
class Solution:
    def jump(self, nums: List[int]) -> int:
        # init
        n = len(nums)
        jumps = 0
        currEnd = 0
        farthest = 0

        # trivial case 
        if n == 1: return 0
        
        # loop through
        for i in range(n-1):
            farthest = max(farthest, i + nums[i])
            
            if i == currEnd:
                jumps += 1
                currEnd = farthest
            
                if currEnd >= n-1:
                    break
        
        return jumps
        
# @lc code=end

