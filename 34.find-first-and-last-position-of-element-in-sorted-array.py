#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.first_bs(nums, target)
        last = self.last_bs(nums, target)

        ans = [-1,-1]
        if first != None: ans[0] = first
        if last != None: ans[1] = last

        return ans
    
    def first_bs(self, arr, target):
        low, high = 0, len(arr)-1
        ans = None

        while low<=high:
            mid = (low+high)//2
            
            if arr[mid] == target:
                ans = mid
                high = mid-1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
    
    def last_bs(self, arr, target):
        low, high = 0, len(arr)-1
        ans = None

        while low<=high:
            mid = (low+high)//2
            
            if arr[mid] == target:
                ans = mid
                low = mid + 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
                
        
        
# @lc code=end

