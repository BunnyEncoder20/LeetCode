class Solution1:
    def longestPalindrome(self, s: str) -> str:
            # helper func
            def expand(l, r):
                palindrome = ""
                while l >= 0 and r <= n-1 and s[l] == s[r]:
                    if (r-l+1) > len(palindrome):
                        palindrome = s[l:r+1]
                    l -= 1
                    r += 1
                return palindrome

            n = len(s)
            maxLenPalin = ""
            for i in range(n):
                oddLenPalin, evenLenPalin = expand(i,i), expand(i,i+1)
                if len(oddLenPalin) > len(maxLenPalin):
                    maxLenPalin = oddLenPalin
                if len(evenLenPalin) > len(maxLenPalin):
                    maxLenPalin = evenLenPalin

            return maxLenPalin
