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
        # Use hash sets to track constraints
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # Pre-fill sets with existing numbers and track empty cells
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty_cells.append((i, j))
                else:
                    val = board[i][j]
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i//3)*3 + j//3].add(val)  # 3x3 grid index
        
        def solve(index=0):
            if index == len(empty_cells):  
                return True  # All cells filled successfully

            row, col = empty_cells[index]
            box_idx = (row // 3) * 3 + (col // 3)
            
            for num in "123456789":
                if num not in rows[row] and num not in cols[col] and num not in boxes[box_idx]:
                    # Place the number
                    board[row][col] = num
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box_idx].add(num)

                    # Recursively solve for the next cell
                    if solve(index + 1):
                        return True
                    
                    # Backtrack
                    board[row][col] = "."
                    rows[row].remove(num)
                    cols[col].remove(num)
                    boxes[box_idx].remove(num)

            return False
        
        solve()  # Start the backtracking process
        
# @lc code=end

