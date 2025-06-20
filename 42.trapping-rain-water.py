#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMaxHeight = self.getPrefixHash(height, n)
        rightMaxHeight = self.getSuffixHash(height, n)

        trapped_rainwater = 0
        for i in range(1,n-1):
            water = min(leftMaxHeight[i], rightMaxHeight[i]) - height[i]
            if water > 0:
                trapped_rainwater += water

        return trapped_rainwater

    def getPrefixHash(self, arr, n):
        prefixHash = [0]*n 
        prefixHash[0] = arr[0]
        for i in range(1,n): 
            prefixHash[i] = max(arr[i], prefixHash[i-1])
        return prefixHash

    def getSuffixHash(self, arr, n):
        suffixHash = [0]*n
        suffixHash[n-1] = arr[n-1]
        for i in range(n-2, -1, -1):
            suffixHash[i] = max(arr[i], suffixHash[i+1])
        return suffixHash

# @lc code=end

