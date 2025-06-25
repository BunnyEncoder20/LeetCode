#
# @lc app=leetcode id=1275 lang=python3
#
# [1275] Find Winner on a Tic Tac Toe Game
#

# @lc code=start
from typing import List
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # player A first ATQ
        player = 'A'

        # represet row and cols sums
        rows, cols = [0]*3, [0]*3

        # represent both diagonal sums
        diag, anti_diag = 0, 0

        winner = None

        for row, col in moves:
            score = 1 if player == 'A' else -1

            # mark the move in rows and cols
            rows[row] += score
            cols[col] += score

            # mark move on diags
            if row == col:
                diag += score
            if row + col == 3-1:
                anti_diag += score
            
            # checks for winner
            # if any of the sums == 3
            if (
                abs(rows[row]) == 3 or 
                abs(cols[col]) == 3 or
                abs(diag) == 3 or
                abs(anti_diag) == 3
            ):
                winner = player
                break
            
            # other players turn
            player = 'B' if player == 'A' else 'A'
        
        if winner:
            return winner
        elif len(moves) == 9:
            return "Draw"
        else:
            return "Pending"
# @lc code=end

