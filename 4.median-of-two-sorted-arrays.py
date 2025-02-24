#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n,m = len(nums1),len(nums2)
        l = n+m                     # merged length
        nums3 = self.merge(nums1, nums2)
        if l % 2 == 0:
            return ((nums3[l//2]) + (nums3[(l//2) - 1])) / 2
        return nums3[l//2]

    def merge(self, arr1, arr2):
        i,j = 0,0
        arr3 = []
        while i<len(arr1) and j<len(arr2):
            if arr1[i] < arr2[j]:
                arr3.append(arr1[i])
                i += 1
            else:
                arr3.append(arr2[j])
                j += 1
        while i<len(arr1):
            arr3.append(arr1[i])
            i+=1
        while j<len(arr2):
            arr3.append(arr2[j])
            j += 1
        return arr3
                
            
        
# @lc code=end

