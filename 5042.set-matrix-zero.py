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

class Solution2:
    '''
        TC: 2 x O(NxM)
        SC: O(n) + O(m)
    '''
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix),len(matrix[0])
        rowMarked = [0]*rows
        colMarked = [0]*cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rowMarked[i] = 1
                    colMarked[j] = 1

        for i in range(rows):
            for j in range(cols):
                if rowMarked[i] or colMarked[j]:
                    matrix[i][j] = 0

        return


class Solution3:
    '''
        TC: 2 x O(N+M) + O(NxM)
        SC: O(1)
    '''
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix),len(matrix[0])
        first_row_zero = any(matrix[0][j]==0 for j in range(cols))
        first_col_zero = any(matrix[i][0]==0 for i in range(rows))

        # Using first row and col as lists, mark zero locations
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Set zeros based on markings
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j] = 0

        # handling the first row and col
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0

        return
