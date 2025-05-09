from collections import deque

class Solution:
    def firstNegInt(self, arr, k): 
        n = len(arr)
        dq = deque()
        result = []
        ans = []
        
        for i in range(n):
            # maintain the window
            # pop before idx from dq
            if dq and dq[0] < i-k+1:
                dq.popleft()
            
            # if -ve, add idx into dq
            if arr[i] < 0:
                dq.append(i)
            
            # if we have k elements,
            # add window negative to ans
            if i >= k-1:
                if dq:
                    ans.append(arr[dq[0]])
                else:
                    ans.append(0)
        return ans 