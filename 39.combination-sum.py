#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def recursive(i, subseq, total):
            # base case 
            if i == n:
                if total == target:
                    res.append(subseq[:])
                return
            
            # base case
            if total > target:
                return 

            # pick
            subseq.append(candidates[i])
            total += candidates[i]
            recursive(i, subseq, total)
            
            # not pick
            subseq.pop()
            total -= candidates[i]
            recursive(i+1, subseq, total)
        
        n = len(candidates)
        res = []
        recursive(0, [], 0)
        return res
    
# @lc code=end

