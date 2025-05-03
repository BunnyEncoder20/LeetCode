import heapq
class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, mat, K):
        heap = []
        result = []
        
        for i in range(K):
            # push first elements of each row:(val, row, col)
            heapq.heappush(heap, (mat[i][0], i, 0))
        
        # pop mini and add next element of row
        while heap:
            val, r, c = heapq.heappop(heap)
            result.append(val)
            
            # if next element in row
            if c+1 < K:
                heapq.heappush(heap, (mat[r][c+1], r, c+1))
        
        return result