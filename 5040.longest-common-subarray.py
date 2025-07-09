class Solution1:
    """
        Recursive
    """
    def longestCommonSubstr(self, s1, s2):
        def recursion(i, j) -> int:
            # base case
            if i < 0 or j < 0:
                return 0

            # chr don't match
            if s1[i] != s2[j]:
                return 0

            # if matched, them only
            # move forward in recursion
            return 1+recursion(i-1, j-1)


        n,m = len(s1), len(s2)
        maxlength = 0
        for i in range(n):
            for j in range(m):
                maxlength = max(maxlength, recursion(i,j))
        return maxlength

from functools import cache
class Solution2:
    '''Memoization'''
    def longestCommonSubstr(self, s1, s2) -> int:
        @cache
        def recursion(i, j) -> int:
            # base case
            if i < 0 or j < 0:
                return 0

            # chr don't match
            if s1[i] != s2[j]:
                return 0

            # if matched, them only
            # move forward in recursion
            return 1+recursion(i-1, j-1)


        n,m = len(s1), len(s2)
        maxlength = 0
        for i in range(n):
            for j in range(m):
                maxlength = max(maxlength, recursion(i,j))
        return maxlength

class Solution3:
    '''Tabulation'''
    def longestCommonSubstr(self, s1, s2) -> int:
        n,m = len(s1), len(s2)

        # DP table
        dp =[[0]*(m + 1) for _ in range(n + 1)]
        maxlength = 0

        for i in range(1, n+1):
            for j in range(1, m+1):
                # chr match, increment substr
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    maxlength = max(maxlength, dp[i][j])

                # else, reset length of substr
                else:
                    dp[i][j] = 0

        return maxlength
