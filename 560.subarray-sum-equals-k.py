#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # hashmap to store count of subarray sums
        sumfpp = {}
    
        # Imp: enter 0 sum with count 1 
        # (represents when we don't take any elements)
        sumfpp[0] = 1

        # count & prefix sum
        count = 0
        prefixSum = 0

        for num in nums:
            prefixSum += num

            # need to remove subarr with 
            toRemove = prefixSum - k

            # if in hashmap
            if toRemove in sumfpp:
                count += sumfpp[toRemove]
            
            # add prefixSum to hashmap, 
            # increase it's count
            if prefixSum in sumfpp:
                sumfpp[prefixSum] += 1
            else:
                sumfpp[prefixSum] = 1
        
        return count
        
# @lc code=end

