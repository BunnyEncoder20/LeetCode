#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Step1: Transpose Matrix
        self.transpose(matrix)

        # Step2: reverse all rows in mat
        for row in matrix:
            row.reverse()
        
        # Step3: matrix rotated
    
    def transpose(self, mat):
        rows, cols = len(mat), len(mat[0])
        for i in range(rows):
            for j in range(i+1, cols):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        
# @lc code=end

