#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#

# @lc code=start
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # sort the products
        products.sort()
        
        # init
        l,r = 0, len(products)-1
        res = []
        
        for i in range(len(searchWord)):
            char = searchWord[i]
            
            # close in on possible products
            while l<=r and (len(products[l]) <= i or products[l][i] != char):
                l += 1
            while l<=r and (len(products[r]) <= i or products[r][i] != char):
                r -= 1
            if l > r:
                res.append([])
            else:
                remaining_products = r-l+1
                res.append(products[l : min(l+3, l+remaining_products)])
        
        return res
                
        
        
# @lc code=end

