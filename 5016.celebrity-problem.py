class Solution:
    def celebrity(self, M):
        n = len(M)
        knowMe = [0]*n
        Iknow = [0]*n
        for i in range(n):
            for j in range(n):
                if M[i][j]:
                    knowMe[j] += 1
                    Iknow[i] += 1
        
        # check for celebrity
        for i in range(n):
            if knowMe[i] == n-1 and Iknow[i] == 0:
                return i
        
        return -1
