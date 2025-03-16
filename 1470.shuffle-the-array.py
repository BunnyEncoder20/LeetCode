#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#

# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # O(1) space approach 
        for i in range(n):
            # make space for the y val in x memory (32 bits)
            # cause atq, x&y shouldn't be more than 1024 = 2^10 hence the 10 bits
            nums[i] = nums[i] << 10
            
            # store the y val in the space made in x memory
            # ∴ we store xi,yi in same position
            nums[i] = nums[i] | nums[i + n]
        
        # extract the vals 
        i, j = n-1, 2*n - 1
        
        # casue we already have y vals, 2nd half can be overwritten now
        # hence we going in reverse order
        while i >= 0:
            # extract y and shift x val back into place
            yi = nums[i] & (2**10 - 1)    
            xi = nums[i] >> 10

            # assign both vals to last positions 
            nums[j] = yi
            nums[j-1] = xi
            
            # update pointers
            i -= 1
            j -= 2
        
        return nums
            
            
        
        
        # O(n) space aprroach
        # res = []
        # for i in range(n):
        #     xi = nums[i]
        #     yi = nums[i+n]
        #     res.append(xi)
        #     res.append(yi)
        # return res
        
# @lc code=end

