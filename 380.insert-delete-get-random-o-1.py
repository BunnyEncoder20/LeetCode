#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
import random
class RandomizedSet:
    def __init__(self):
        self.mpp = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.mpp:
            return False
        
        self.mpp[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mpp:
            return False
        
        idx = self.mpp[val]
        last_val = self.nums[-1]

        # del (overwrite) val with last num
        # and update mpp
        self.nums[idx] = last_val
        self.mpp[last_val] = idx

        # remove extra last val at end
        # remove val entry in mpp
        self.nums.pop()
        del self.mpp[val]
        
        return True
        

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.nums) - 1)
        return self.nums[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

