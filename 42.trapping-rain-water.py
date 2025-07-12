#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List

class Solution1:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = self.getPrefixMaximum(height, n)
        rightMax = self.getSuffixMaximum(height, n)

        trappedWater = 0
        for i in range(1,n-1):
            water = min(leftMax[i], rightMax[i]) - height[i]
            if water > 0: trappedWater += water

        return trappedWater

    def getPrefixMaximum(self, height, n) -> List:
        prefixMaximum = [0]*n
        prefixMaximum[0] = height[0]
        for i in range(1, n):
            prefixMaximum[i] = max(prefixMaximum[i-1], height[i])
        return prefixMaximum

    def getSuffixMaximum(self, height, n) -> List:
        suffixMaximum = [0]*n
        suffixMaximum[-1] = height[-1]
        for i in range(n-2, -1, -1):
            suffixMaximum[i] = max(suffixMaximum[i+1], height[i])
        return suffixMaximum


class Solution2:
    def trap(self, height: List[int]) -> int:
        # 2 pointers
        left, right = 0, len(height)-1
        leftMax, rightMax = 0, 0
        trapped_rainwater = 0

        # always move the smaller ptr
        while left<right:
            if height[left] <= height[right]:
                if height[left] < leftMax:
                    trapped_rainwater += leftMax - height[left]
                else:
                    leftMax = height[left]
                left += 1
            else:
                if height[right] < rightMax:
                    trapped_rainwater += rightMax - height[right]
                else:
                    rightMax = height[right]
                right -= 1

        return trapped_rainwater

# @lc code=end
