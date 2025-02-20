#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low,high = 0, len(nums)-1
        
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low = mid+1
            else:
                high = mid-1
        
        return -1
                
        
        
# @lc code=end

