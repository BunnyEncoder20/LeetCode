#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def solve(self, mat: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(x,y):
            return (
                0 <= x < rows and
                0 <= y < cols and
                mat[x][y] == 'O'
            )
        
        def dfs(x,y):
            vis[x][y] = True
            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if isValid(nx,ny) and not vis[nx][ny]:
                    dfs(nx,ny)
        
        # init
        rows,cols = len(mat),len(mat[0])
        vis = [[False] * cols for _ in range(rows)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        # traverse the top and bottom bondary and DFS any 'O' you can find
        for j in range(cols):
            # top boundary
            if not vis[0][j] and mat[0][j] == 'O':
                dfs(0,j)
            # bottom boundary
            if not vis[rows-1][j] and mat[rows-1][j] == 'O':
                dfs(rows-1,j)
        
        # Traverse the left and right boundary and DFS any 'O' you can find
        for i in range(rows):
            # left boundary
            if not vis[i][0] and mat[i][0] == 'O':
                dfs(i,0)
            if not vis[i][cols-1] and mat[i][cols-1] == 'O':
                dfs(i,cols-1)
        
        # traverse the remaingin matrix and eliminate any 'O'
        for i in range(1,rows-1):
            for j in range(1,cols-1):
                if mat[i][j] == 'O' and not vis[i][j]:
                    mat[i][j] = 'X'
        
        return
        
        
# @lc code=end

