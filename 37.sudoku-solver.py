#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def canFit(board, row, col, digit):
            # check row and col for same digit
            for i in range(9):
                if board[row][i] == digit or board[i][col] == digit:
                    return False
            
            # check current block
            brow,bcol = (row//3)*3, (col//3)*3
            for i in range(brow, brow+3):
                for j in range(bcol, bcol+3):
                    if board[i][j] == digit:
                        return False
            
            return True

        def solve(board):
            n = 9       # size of sudoku board
            for i in range(n):
                for j in range(n):
                    # found an empty cell
                    if board[i][j] == ".":
                        for digit in "123456789":
                            # try to fit digit
                            if canFit(board, i, j, digit):
                                # place the digit and see if we get soln
                                board[i][j] = digit

                                # recursively place on other position
                                if solve(board):
                                    return True
                                
                                # backtrack cause could't find soln with above config
                                board[i][j] = "."

                        # No digits could be placed
                        return False

            # all cells traversed
            return True
        
        # call the function
        solve(board)
        
# @lc code=end

