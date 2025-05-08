class Solution:
    def celebrity(self, M):
        n = len(M)
        top = 0
        down = n-1
        
        while top < down:
            # if top knows down, top cannot be celebrity
            if M[top][down]:
                top += 1

            # if down knows top, down cannot be celebrity
            elif M[down][top]:
                down -= 1
            
            # if both don't know eachother,
            # both cannot be celebrity
            else:
                top += 1
                down -= 1
        
        # didn't find celebrity 
        if top > down: 
            return -1

        # else top == down
        # verify
        for i in range(n):
            if i == top: continue

            # if top knows i or i doesn't know top,
            # top is not a celeb
            if M[top][i] or not M[i][top]:
                return -1

        # verified celeb
        return top

if __name__ == "__main__":
    M = [
        [0, 1, 1, 0], 
        [0, 0, 0, 0], 
        [1, 1, 0, 0], 
        [0, 1, 1, 0]
    ]
    print(Solution().celebrity(M))
