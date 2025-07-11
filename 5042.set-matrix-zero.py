from typing import List

class Solution1:
    '''
        TC: O(NxM) x O(N+M) + O(NxM) ≈ O(n^3)
        SC: O(1)
    '''
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])

        # helper func
        def markrows(col):
            for i in range(rows):
                if matrix[i][col] != 0:
                    matrix[i][col] = -1
        def markcols(row):
            for j in range(cols):
                if matrix[row][j] != 0:
                    matrix[row][j] = -1

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    markrows(j)
                    markcols(i)

        # convert all -1 to 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0

        return
