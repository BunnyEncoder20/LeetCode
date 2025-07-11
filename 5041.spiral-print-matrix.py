class Solution:
    def spiralPrint(self, mat):
        rows, cols = len(mat), len(mat[0])

        # pointers
        top, left = 0, 0
        down, right = rows-1, cols-1

        ans = []

        while top<=down and left<=right:
            # left to right (top row →)
            for i in range(left, right+1):
                ans.append(mat[top][i])
            top += 1

            # top to bottom (right col ↓)
            for i in range(top, down+1):
                ans.append(mat[i][right])
            right -= 1

            # right to left (bottom row ←)
            if top <= down:
                for i in range(right, left-1, -1):
                    ans.append(mat[down][i])
                down -= 1

            # bottom to top (left col ↑)
            if left <= right:
                for i in range(down, top-1, -1):
                    ans.append(mat[i][left])
                left += 1

        return ans
