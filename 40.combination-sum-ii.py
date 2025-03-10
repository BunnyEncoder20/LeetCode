#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def recursively(i, subseq, total):
            # base cases
            if i == n: 
                if total == target:
                    res.append(subseq[:]) 
                return 
            if total > target:
                return 
            
            # normally
            # pick
            subseq.append(candidates[i])
            total += candidates[i]
            recursively(i+1, subseq, total)
            subseq.pop()
            total -= candidates[i]
            
            # don't pick (skip dups)
            while i < n-1 and candidates[i] == candidates[i+1]:
              i += 1
              
            recursively(i+1, subseq, total)
            
        candidates.sort()
        n = len(candidates)
        res = []
        recursively(0, [], 0)
        return res
# @lc code=end

