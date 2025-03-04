#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def revArr(i,j):
            while i<j:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j-=1
        n = len(nums)
        k = k%len(nums)
        revArr(0,n-1)
        revArr(0,k-1)
        revArr(k,n-1)
        
# @lc code=end

