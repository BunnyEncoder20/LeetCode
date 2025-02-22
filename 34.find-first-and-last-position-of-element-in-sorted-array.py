#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1,-1]
        
        lb = self.lowerBound(nums, target)
        ub = self.upperBound(nums, target)
        
        # if no occurance of element 
        if lb == len(nums) or nums[lb] != target:
            return [-1,-1]

        return [lb, ub-1]

    def lowerBound(self, nums, target):
        lb = len(nums)
        low,high = 0, len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] >= target:
                lb = mid
                high = mid-1
            else:
                low = mid+1 
        return lb

    def upperBound(self, nums, target):
        ub = len(nums)
        low,high = 0, len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] > target:
                ub = mid
                high = mid-1
            else:
                low = mid+1 
        return ub
                
        
        
# @lc code=end

