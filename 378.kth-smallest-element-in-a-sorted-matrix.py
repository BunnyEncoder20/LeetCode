#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
import bisect
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def upperBound(candidate, arr):
            low, high = 0, len(arr)-1
            while low<=high:
                mid = (low+high)//2
                if arr[mid] > candidate:
                    high = mid-1
                else:
                    low = mid+1
            return low
        
        def countLower(candidate):
            count = 0
            for row in matrix:
                # count += upperBound(candidate, row)
                count += bisect.bisect_right(row, candidate)
            return count
        
        # init
        n = len(matrix)
        low = matrix[0][0]
        high = matrix[n-1][n-1]
        
        # BS the range
        while low <= high:
            mid = (low + high)//2
            lowerCount = countLower(mid)
            
            # check
            if lowerCount < k:
                low = mid+1
            else:
                high = mid-1
        
        return low
        
# @lc code=end

