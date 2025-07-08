class Solution:
    def areRotations(self, s1, s2):
        # trivial cases
        if len(s1) != len(s2): return False
        if s1 == s2: return True

        # check if s2 is substring of s1+s1
        return s2 in s1+s1

sol = Solution()
print(sol.areRotations("waterbottle", "erbottlewat"))   # True
print(sol.areRotations("abc", "cab"))                   # True
print(sol.areRotations("abc", "acb"))                   # False