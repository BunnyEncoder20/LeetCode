'''
KnightL is a chess piece that moves in an L shape. We define the possible moves of KnightLa, b) as any movement from some position (x1, Y1) to some (x2, Y2) satisfying either of the following:
• X2 = x1 = a and y2 = y1 = b, or
• x2 = x1 = b and y2 = y1 =a
Note that (a, b) and (b, a) allow for the same exact set of movements.
Given the value of n for ann X n chessboard, answer the following question for each (a, b) pair where
1≤a, b< n:
• What is the minimum number of moves it takes for KnightLa, b) to get from position (0, 0) to position (n - 1, n - 1)? If it's not possible for the Knight to reach that destination, the answer is - 1 instead.
Then print the answer for each KnightLa, b) according to the Output Format specified below.
'''

from collections import deque
def knightlOnAChessboard(n):
    def minMoves(n, i, j):
        moves = [(i, j), (i, -j), (-i, j), (-i, -j), (j, i), (j, -i), (-j, i), (-j, -i)]
        q = deque([(0, 0, 0)]) # x,y,moves
        vis = set([(0,0)])
        
        while q:
            x,y, steps = q.popleft()
            
            # reached target
            if x == n-1 and y == n-1:
                return steps
            
            # explore next moves
            for dx, dy in moves:
                nx, ny = x+dx, y+dy
                if (0 <= nx < n and 0 <= ny < n and (nx,ny) not in vis):
                    vis.add((nx, ny))
                    q.append((nx, ny, steps+1))
        # [n-1][n-1] not reachable
        return -1     
        
        
    res = [[-1] * (n-1) for _ in range(n-1)]
    
    for a in range(1,n):
        for b in range(a, n):
            moves = minMoves(n, a, b)
            if moves > 0:
                res[a-1][b-1] = moves
                res[b-1][a-1] = moves # symetry a,b = b,a
    
    # construct ans
    ans = []
    for row in res:
        ans.append(str(moves) for moves in row)
    return ans