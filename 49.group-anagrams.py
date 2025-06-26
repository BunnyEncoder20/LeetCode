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
            # count vector
            count = [0]*26  # a....z counts
            
            for ch in word:
                # count[ch_idx] += 1
                count[ord(ch) - ord('a')] += 1
            
            key = tuple(count)  # non hashable list cannot be dict key
            results[key].append(word)
        
        return list(results.values())
            
                    

# @lc code=end

