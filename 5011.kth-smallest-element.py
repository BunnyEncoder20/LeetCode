import heapq
class Solution:

    def kthSmallest(self, arr,k):
        maxheap = [-arr[i] for i in range(k)]
        heapq.heapify(maxheap)
        
        for i in range(k, len(arr)):
            if arr[i] < -maxheap[0]:
                heapq.heappushpop(maxheap, -arr[i])

print(Solution().kthSmallest([7,10,4,3,20,15,3], 3))