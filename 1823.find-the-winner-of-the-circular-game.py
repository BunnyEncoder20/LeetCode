#
# @lc app=leetcode id=1823 lang=python3
#
# [1823] Find the Winner of the Circular Game
#

# @lc code=start
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1,n+1))
        skip = k-1      # casuse k is given as 1-based idx
        i = skip        # idx to eliminate
        while len(friends) > 1:
            # eliminate the idx
            friends.pop(i)
            # go to next idx. Using % to wrap idxs
            i = (i + skip) % len(friends)
        
        return friends[0]
        
# @lc code=end

