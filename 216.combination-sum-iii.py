#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def recursive(sum, subseq, last):
            # base case +ve
            if len(subseq) == k and sum == n:
                ans.append(subseq[:])
                return

            # base case -ve
            if len(subseq) > k  or sum > n:
                return
            
            # normally
            for digit in range(last+1, 10):
                subseq.append(digit)
                recursive(sum + digit, subseq, digit)
                subseq.pop()
                 
        ans = []
        recursive(0, [], 0)
        return ans 
# @lc code=end

