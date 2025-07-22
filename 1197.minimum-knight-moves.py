from collections import deque
class Solution:
    def minStepToReachTarget(self, knightPos, targetPos, N):
        # convert to 0 based indexing
        kx, ky = knightPos[0]-1, knightPos[1]-1
        tx, ty = targetPos[0]-1, targetPos[1]-1

        # trivial case
        if kx == tx and ky == ty:
            return 0

        # init for grid BFS
        directions = [(2, 1), (2, -1), (-2, 1), (-2, -1),(1, -2), (-1, -2), (1, 2), (-1, 2)]
        visited = [[0]*N for _ in range(N)]

        # insert starting point
        q = deque([(kx,ky,0)])  # x,y,steps
        visited[kx][ky] = 1


        # helper func
        def isVaid(i, j):
            return (
                0<=i<N and
                0<=j<N and
                not visited[i][j]
            )


        while q:
            x,y,steps = q.popleft()

            # check all posible moves
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if isVaid(nx, ny):
                    # check if found target
                    if nx == tx and ny == ty:
                        return steps+1

                    # else process node
                    visited[nx][ny] = 1
                    q.append((nx,ny,steps+1))

        return -1


if __name__ == '__main__':
    solution = Solution()
    tests = [
        {"case": 1, "knightPos": [4, 5], "targetPos": [1, 1], "N": 6, "expected": 3},
        {"case": 2, "knightPos": [1, 1], "targetPos": [1, 1], "N": 8, "expected": 0},
        {"case": 3, "knightPos": [1, 1], "targetPos": [1, 2], "N": 2, "expected": -1},
        {"case": 4, "knightPos": [1, 1], "targetPos": [3, 2], "N": 8, "expected": 1},
        {"case": 5, "knightPos": [1, 1], "targetPos": [8, 8], "N": 8, "expected": 6},
        {"case": 6, "knightPos": [7, 7], "targetPos": [2, 3], "N": 8, "expected": 3},
    ]

    for test in tests:
        knightPos = test["knightPos"]
        targetPos = test["targetPos"]
        N = test["N"]
        expected = test["expected"]
        output = solution.minStepToReachTarget(knightPos, targetPos, N)
        status = "✅ Passed" if output == expected else "❌ Failed"
        print(f"Test{test['case']}: input: knightPos={knightPos}, targetPos={targetPos}, N={N} | output: {output} | expected: {expected} | {status}")
