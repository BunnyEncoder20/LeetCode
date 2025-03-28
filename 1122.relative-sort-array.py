#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # init 
        arr2_set = set(arr2)
        fpp = {}
        end = []

        # construct fpp and end
        for n in arr1:
            if n not in arr2_set:
                end.append(n)
            else:
                fpp[n] = fpp.get(n, 0) + 1
        end.sort()
        
        # re arrange arr1
        ans = []
        for n in arr2:
            for _ in range(fpp[n]):
                ans.append(n)
        
        return ans + end
            
        
# @lc code=end

