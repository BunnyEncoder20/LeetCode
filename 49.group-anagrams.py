#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from typing import List
from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        results = defaultdict(list)

        for word in words:
            group_key = tuple(sorted(word))
            results[group_key].append(word)
        
        return list(results.values())
                    

# @lc code=end

