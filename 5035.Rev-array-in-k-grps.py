class Solution:
    def ReverseInGroups(self, arr, k):
        n = len(arr)
        for i in range(0, n, k):
            if i + k <= n:
                # rev k group subarray
                arr[i:i+k] = arr[i:i+k][::-1]
        return arr


Solution().ReverseInGroups([1,2,3,4,5,6,7,8,9,10], 3)