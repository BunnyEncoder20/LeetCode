#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        n,m = len(nums1), len(nums2)
        p1,p2 = 0,0
        res = set()
        
        while p1 < n and p2 < m:
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                res.add(nums1[p1])
                p1 += 1
                p2 += 1
        
        return list(res)
        
        
# @lc code=end

