#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        # 2 pointers approach
        left, right = 0, len(height)-1
        leftMax, rightMax = 0, 0
        trapped_rainwater = 0

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

