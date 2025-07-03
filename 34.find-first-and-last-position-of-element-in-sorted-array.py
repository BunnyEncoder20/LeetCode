#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = []
        ans.append(self.first_pos(nums, target))
        ans.append(self.last_pos(nums, target))
        return ans
    
    def first_pos(self, nums, target):
        '''lowerbound'''
        low, high = 0, len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] >= target:
                high = mid-1
            else:
                low = mid+1

        if low < len(nums) and nums[low] == target:
            return low
        return -1

    def last_pos(self, nums, target):
        '''upperbound'''
        low, high = 0, len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] > target:
                high = mid-1
            else:
                low = mid+1

        if low > 0 and nums[low-1] == target:
            return low-1
        return -1
        
        
# @lc code=end
