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
        original = defaultdict(list)
        for i,n in enumerate(nums):
            original[n].append(i)
            
        nums.sort()
        l,r = 0,len(nums)-1
        
        while l < r:
            summ = nums[l] + nums[r]
            if summ == target:
                # if dups
                if nums[l] == nums[r]:
                    return original[nums[l]][0:2]
                return [original[nums[l]].pop(0), original[nums[r]].pop(0)]
            elif summ < target:
                l += 1
            else:
                r -= 1
        
        return [-1,-1]
        
        
        
# @lc code=end

