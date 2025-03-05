#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def isSafe(self, board, row, col):
      # check left upper diagonal
      r,c = row,col
      while r >= 0 and c >= 0:
        if board[r][c] == "Q": return False
        r -= 1
        c -= 1
        
      # check left side
      r,c = row,col
      while c >= 0:
        if board[r][c] == "Q": return False
        c -= 1
        
      # check left lower diagonal
      r,c = row,col
      while r < len(board) and c >= 0:
        if board[r][c] == "Q": return False
        r += 1
        c -= 1
        
      # no Queens in attacking pos
      return True
                
        
    def placeQueens(self, col, ans, board):
      # base case 
      if col == len(board):
          # add board to ans
          ans.append(board[:])
          return
      
      # normally
      for row in range(len(board)):
        if self.isSafe(board, row, col):
          # if the position is safe, place Q
          board[row] = board[row][:col]+"Q"+board[row][col+1:]

          # recursively go to next col and try to place another Q
          self.placeQueens(col+1,ans,board)
          
          # remove Q for backtracking
          board[row] = board[row][:col]+"."+board[row][col+1:]
                

        
    def solveNQueens(self, n: int) -> List[List[str]]:
      board = ["."*n for _ in range(n)] # "....." for _ i range(n)
      ans = []
      self.placeQueens(0, ans, board)
      return ans
        
        
# @lc code=end

