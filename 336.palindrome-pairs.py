#
# @lc app=leetcode id=336 lang=python3
#
# [336] Palindrome Pairs
#

# @lc code=start
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans = []
        if not words: return ans
        n = len(words)
        for i in range(n):
            for j in range(i+1,n):
                temp1 = words[i]+words[j]
                temp2 = words[j]+words[i]
                if self.isPalindrome(temp1):
                    ans.append([i,j])
                if self.isPalindrome(temp2):
                    ans.append([j,i])

        return ans

    def isPalindrome(self, word):
        i,j = 0,len(word)-1
        while i<=j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        return True
                
        
        
        
# @lc code=end

