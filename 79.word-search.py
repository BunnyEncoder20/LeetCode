class Solution:
    def exist(self, board, word):
        def dfs(r,c,i):
            # base case: +ve
            if i == len(word):
                return True

            # base case: -ve
            if not (
                0<=r<rows and
                0<=c<cols and
                board[r][c] == word[i]
            ): return False

            # move onto next letters in adj cells
            originalLetter = board[r][c]
            board[r][c] = "*"
            result = any(
                dfs(r+dr, c+dc, i+1) for dr,dc in directions
            )
            board[r][c] = originalLetter
            return result

        rows, cols = len(board),len(board[0])
        directions = [(-1,0),(0,-1),(0,1),(1,0)]
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r,c,0): return True
        return False
