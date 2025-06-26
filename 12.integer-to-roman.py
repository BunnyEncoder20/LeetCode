#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        # mapping (will be going from MSB to LSB)
        value_symbol_mapping = [
            (1000, 'M'),(900, 'CM'),(500, 'D'), 
            (400, 'CD'),(100, 'C'), (90, 'XC'), 
            (50, 'L'),  (40, 'XL'), (10, 'X'),
            (9, 'IX'),  (5, 'V'),   (4, 'IV'), 
            (1, 'I')
        ]

        resultant = ""
        for value, symbol in value_symbol_mapping:
            # 2000 // 1000 = multiple x RN
            # = 2 * 'M = 'MM'
            # if multiple = 0, no symbol will be added
            multiple = num // value
            resultant += (symbol * multiple)

            # update number
            num %= value
        
        return resultant


# @lc code=end

