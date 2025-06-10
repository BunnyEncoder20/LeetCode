#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        prevColor = image[sr][sc]
        # trivial case
        if prevColor == color: return image

        # constants
        rows, cols = len(image), len(image[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        # good practice not to alter original data, make copy
        ansImage = [row[:] for row in image]
        
        def dfs(i, j):
            # base case
            if (
                not (0<=i<rows) or 
                not (0<=j<cols) or
                ansImage[i][j] != prevColor
            ): return

            # recolor
            ansImage[i][j] = color

            # dfs neighbours
            for di, dj in directions:
                dfs(i+di, j+dj)
        
        dfs(sr,sc)
        return ansImage
        
# @lc code=end

