#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
from typing import List
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        '''This is the same as Book Allocation Problem'''
        # helper func
        def numberStudents(maxPages):
            students = 1
            pages_with_student = 0

            for pages in nums:
                # if student can have more pages
                if pages_with_student + pages <= maxPages:
                    pages_with_student += pages
                
                # else add another student
                else:
                    students += 1
                    pages_with_student = pages
            
            return students

        # edge case: books less than students
        if len(nums) < k: return -1

        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = (low+high)//2
            
            if numberStudents(mid) > k:
                low = mid+1
            else:
                high = mid-1

        # low starts at pages not possible
        # high starts at pages possible
        # Hence according to BS opposite Polarity
        return low


        
# @lc code=end

