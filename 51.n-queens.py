#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ["."*n for _ in range(n)]
        ans = []
        self.placeNQueens(0, board, ans)
        return ans
    
    def placeNQueens(self, col, board, ans):
        n = len(board)

        # base case
        if col == n:
            ans.append([row for row in board])
            return
        
        # try to place Q in each row for this col
        for row in range(n):
            if self.canPlace(board, row, col):
                board[row] = board[row][:col] + "Q" + board[row][col+1:]
                self.placeNQueens(col+1, board, ans)
                board[row] = board[row][:col] + "." + board[row][col+1:]
        
        return
    
    def canPlace(self, board, row, col):
        n = len(board)

        # check Upper diagonal dir
        i, j = row, col
        while i>=0 and j>=0:
            if board[i][j] == 'Q': return False
            i -= 1
            j -= 1
        
        # check left side of row
        j = col
        while j>= 0:
            if board[row][j] == 'Q': return False
            j -= 1
        
        # check lower diagonal dir
        i,j = row, col
        while i<n and j>=0:
            if board[i][j] == 'Q': return False
            i += 1
            j -= 1

        return True        
        
# @lc code=end

