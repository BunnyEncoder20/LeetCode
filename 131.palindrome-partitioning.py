#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # trivial case
        n = len(s)
        if n == 0: return s
        
        def dfs(idx, path):
            # base case
            if idx == n:
                res.append(path[:])
                return 

            # normally
            for i in range(idx, len(s)):
                substring = s[idx:i+1]
                if isPalindrome(substring):
                    path.append(substring)
                    dfs(i+1, path)
                    path.pop()
        
        def isPalindrome(word):
            l,r = 0,len(word)-1
            while l<=r:
                if word[l] != word[r]: return False
                l += 1
                r -= 1 
            return True

        res = []
        dfs(0, [])
        return res
            
        
# @lc code=end

